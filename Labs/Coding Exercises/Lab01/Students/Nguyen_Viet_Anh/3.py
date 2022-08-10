from datetime import datetime
c = datetime.now()

class CustomDate:
    def get_date(self):
        return c.strftime("%m/%d/%Y")
    def get_time(self):
        return c.strftime("%H:%M:%S")
now = CustomDate()
print(now.get_date())
print(now.get_time())
