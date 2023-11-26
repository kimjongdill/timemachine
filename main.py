import RotaryEncoder.RotaryEncoder as RotaryEncoder
import DateDialHandler.DateDialHandler as DateDialHandler
import ProxySetter.ProxySetter as ProxySetter
import DateInputs.DateInputs as DateInputs
import ScreenDriver.ScreenDriver as ScreenDriver

DATE_DIAL_CLK = 17
DATE_DIAL_DT = 18
DATE_DIAL_SW = 22

def main():
    proxySetter = ProxySetter("localhost", "8888")
    dateInputs = DateInputs()
    screenDriver = ScreenDriver()
    dialHandler = DateDialHandler(proxySetter, dateInputs, screenDriver)

    dateDial = RotaryEncoder(
        clockPin = DATE_DIAL_CLK,
        dataPin = DATE_DIAL_DT,
        buttonPin = DATE_DIAL_SW,
        Handler = dialHandler
    )

    while 1:
        dateDial.read()
    
    return

if __name__ == '__main__': 
    main()