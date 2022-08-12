from datetime import datetime


class yourtime:
    dates = 0 
    times = 0
    def __init__(self , dates, times):
        self.dates = dates
        self.times = times
    def getdate(self):
        print(self.dates)
    def gettime(self):
        print(self.times)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
nows = yourtime(date,time)
nows.getdate()
nows.gettime()

