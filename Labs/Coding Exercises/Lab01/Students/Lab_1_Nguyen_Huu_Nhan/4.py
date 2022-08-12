from datetime import datetime
class DateHandler:
    def format_date(self):
        return self.strftime("%d/%m/%Y")
    def get_days_between(self1, self2):
        return (self2-self1).days
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)
print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:",
 DateHandler.get_days_between(start_date, end_date))