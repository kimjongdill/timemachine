import RPi.GPIO as GPIO
import time

CLOCKWISE = 1
COUNTER_CLOCKWISE = -1
INVALID = 0

SAMPLE_FILTER_MASK = 0xFFFFFFFFFFFFFFFFFFFFF
VALID_FALLING = SAMPLE_FILTER_MASK ^ 0x1
VALID_RISING = 1

RISING = 2
FALLING = 3
STABLE_TRUE = 1
STABLE_FALSE = 0
UNSTABLE = -1

###

def _validVectorTransitions(clockState, dataState):
    direction = INVALID
    
    if(clockState == RISING):
        if(dataState == STABLE_TRUE):
            direction = COUNTER_CLOCKWISE
        elif(dataState == STABLE_FALSE):
            direction = CLOCKWISE
    if(clockState == FALLING):
        if(dataState == STABLE_FALSE):
            direction = COUNTER_CLOCKWISE
        elif(dataState == STABLE_TRUE):
            direction = CLOCKWISE
    
    return direction

###

def _stateFromFilter(filter):
    if(filter == VALID_RISING):
        return RISING
    if(filter == VALID_FALLING):
        return FALLING
    if(filter == 0):
        return STABLE_FALSE
    if(filter == SAMPLE_FILTER_MASK):
        return STABLE_TRUE
    return UNSTABLE


class RotaryEncoder: 

    def __init__(self, clockPin, dataPin, buttonPin, Handler):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.buttonPin = buttonPin
        self.handler = Handler
        self.buttonFilter = SAMPLE_FILTER_MASK
        self.clockFilter = 0xAAAA
        self.dataFilter = 0xAAAA
        return

    def readDial(self): 
        clock = GPIO.input(self.clockPin)
        data = GPIO.input(self.dataPin)
    
        self.clockFilter = (self.clockFilter << 1 | clock) & SAMPLE_FILTER_MASK
        self.dataFilter = (self.dataFilter << 1 | data) & SAMPLE_FILTER_MASK

        clockState = _stateFromFilter(self.clockFilter)
        dataState = _stateFromFilter(self.dataFilter)

        ## Determine Direction
        direction = _validVectorTransitions(clockState, dataState)

        if(direction == CLOCKWISE): 
            self.handler.handleClockwise()
        elif(direction == COUNTER_CLOCKWISE): 
            self.handler.handleCounterClockwise()



    def readButton(self): 
        button = GPIO.input(self.buttonPin)
        self.buttonFilter = ((self.buttonFilter << 1) | button) & SAMPLE_FILTER_MASK
        # print(self.buttonFilter)
        if(self.buttonFilter == VALID_FALLING):
            self.handler.handleClick()


    def read(self): 
        self.readDial()
        self.readButton()

