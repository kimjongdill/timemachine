import time
from datetime import datetime,date,timedelta
from dateutil.relativedelta import relativedelta

class DateInputs: 
    def __init__(self):
        self.currentDate = date(1999,12,31)
        self.currentField = "YEAR"

    def setDate(self, dateString): 
        self.currentDate = datetime.strptime(dateString, "%Y%m%d")

    def addTime(self, number): 
        if self.currentField == "YEAR":
            self.currentDate = self.currentDate + relativedelta(years=number)
                
        elif self.currentField == "MONTH":
            self.currentDate = self.currentDate + relativedelta(months=number)
            
        elif self.currentField == "DAY":
            self.currentDate = self.currentDate + timedelta(days=number)
                

    def toggleField(self):
        if self.currentField == "YEAR":
            self.currentField = "MONTH"

        elif self.currentField == "MONTH":
            self.currentField = "DAY"

        elif self.currentField == "DAY":
            self.currentField = "YEAR"
                

    def toString(self): 
        dateString = ""
        if self.currentField == "YEAR":
            dateString = "%Y.%m%d"

        elif self.currentField == "MONTH":
            dateString = "%Y%m.%d"

        elif self.currentField == "DAY":
            dateString = "%Y%m%d."
        
        return self.currentDate.strftime(dateString)
    
    def toStringNoDot(self):
        return self.currentDate.strftime("%Y%m%d")
