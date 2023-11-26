
from threading import Timer

TIMER_WAIT_SECONDS = 3

def staticMethod(): 
    print("I Ran")

class DateDialHandler:

    def __init__(self, proxySetter, dateInputs, screenDriver):
        self.ProxySetter = proxySetter
        self.DateInputs = dateInputs
        self.ScreenDriver = screenDriver
        self.timer = Timer(0, self.changeProxy)
        self.timer.start()

    def changeProxy(self):
        attemptedDate = self.DateInputs.toStringNoDot()
        try: 
            returnedDate = self.ProxySetter.changeDate(attemptedDate)
            print("proxy successfully updated to date: " + returnedDate)
            self.DateInputs.setDate(returnedDate)
        except: 
            print("proxy failed to update for date: " + attemptedDate)
        self.ScreenDriver.write(self.DateInputs.toString())

    def changeProxyDelay(self): 
        self.timer.cancel()
        self.timer = Timer(TIMER_WAIT_SECONDS, self.changeProxy)
        self.timer.start()

    def incrementTime(self, count): 
        self.DateInputs.addTime(count)
        outputText = self.DateInputs.toString()
        self.ScreenDriver.write(outputText)

    def handleClockwise(self): 
        self.incrementTime(1)
        self.changeProxyDelay()
    
    def handleCounterClockwise(self):
        self.incrementTime(-1)
        self.changeProxyDelay()

    def handleClick(self):
        self.DateInputs.toggleField()
        outputText = self.DateInputs.toString()
        self.ScreenDriver.write(outputText)