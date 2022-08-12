from datetime import datetime
a = datetime.now()
class CustomDate:
    def get_date(self):
        return f"{ a.day:02d}/{a.month:02d}/{a.year:04d}"
    def get_time(self):
        return f"{a.hour:02d}:{a.minute:02d}:{a.second:02d}"
now = CustomDate()
print(now.get_date())
print(now.get_time())