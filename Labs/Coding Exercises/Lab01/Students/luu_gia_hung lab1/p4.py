from datetime import date, datetime

class Datehandle:
    day1 = 0
    day2 = 0
    def __init__(self , day1 , day2):
        self.day1 = day1
        self.day2 = day2
    def minus():
        print(day1 - day2)

year1 = int(input("Enter your first year"))
month1 = int(input("Enter your first month"))
date1 = int(input("Enter your first date"))

year2 = int(input("Enter your second year"))
month2 = int(input("Enter your second month"))
date2 = int(input("Enter your second date"))

day1 = datetime(year1,month1,date1)
day2 = datetime(year2,month2,date2)

timehan = Datehandle(day1 , day2)
Datehandle.minus()