#bai1
class Employee:
    def __init__(self, name, job):
        self.name=name
        self.job=job
    def say_hi(self):
        print("hi, my name is "+ self.name)
    def tell_position(self):
        print("I am a "+ self.job)
    
john = Employee("John", "Software Engineer")
john.say_hi()
john.tell_position()

#bai2
class rectangle:
   
    def __init__(self,height,width):
        self.height= int(height)
        self.width= int(width)
    def dientich(self):
        return(self.height* self.width)
    def chuvi(self):
        return(2*(self.height+self.width))
class circle:
    def __init__(self,radius):
        self.radius= int(radius)
    def dientich(self):
        return(self.radius*3.14)
    def chuvi(self):
        return(2*3.14*self.radius)


shape= input("shape (rectangle|circle):")
if shape=="rectangle":
    height= input("chieu dai?")
    width= input("chieu rong?")
    output= rectangle(height,width)
elif shape=="circle":
    radius= input("ban kinh?")
    output=circle(radius)
else:
    print("invalid")
print(output.dientich())
print(output.chuvi())

#bai3
class CustomDate():
    def __init__ (self,day,month,year,hour,minute,second):
        self.day=day
        self.month=month
        self.year=year
        self.hour=hour
        self.minute=minute
        self.second=second
    def get_date(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year:04d}")
    def get_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

from datetime import datetime
now = datetime.now()
now= CustomDate(now.day,now.month,now.year,now.hour,now.minute,now.second)
now.get_date()
now.get_time()

#bai4
class DateHandler():
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    def format_date(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year:04d}")
    def get_days_between(start_date,end_date):
        return(abs((start_date-end_date).days))
        
        
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:",
       DateHandler.get_days_between(start_date, end_date))