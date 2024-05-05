from services import ITimeService 
from ITimeService import ITimeService
import time

class TimeService(ITimeService):

    def __init__(self,time_velocity = 288):
        self.time_velocity = time_velocity
        self.minutes = 0
        self.hours = 0
        self.days = 0
        self.months = 0
        self.years = 0
        self.total_days = 0

    def advance_time(self):
        self.minutes += self.time_velocity
        if self.minutes > 59:
            self.hours += self.minutes // 60
            self.minutes = self.minutes - (60 * (self.minutes // 60))
            if self.hours > 23:
                self.days += self.hours // 24  
                self.hours = self.hours - (24 * (self.hours // 24))              
                if self.days > 365:
                        self.years += self.days // 365
                        self.days = self.days - (365 * (self.days // 365))


    def adjust_time_velocity(self,new_velocity):
        self.time_velocity = new_velocity

    def get_time(self):
        return f'{self.minutes} minutes, {self.hours} hours, {self.days} days and {self.years} years have passed.'

seconds = 0  
myTime = TimeService(288) 
while True:
    print(myTime.get_time())
    time.sleep(1)
    seconds += 1
    if seconds % 60 == 1:
        myTime.advance_time()
    if seconds > 180:
        break




