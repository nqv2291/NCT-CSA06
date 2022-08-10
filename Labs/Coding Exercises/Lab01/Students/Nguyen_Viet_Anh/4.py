from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)
class DateHandler:
    @classmethod
    def format_date(cls,year):
        return year.strftime("%m/%d/%Y")
    def get_days_between(date1, date2):
        delta = date2-date1
        return delta.days



print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:", DateHandler.get_days_between(start_date, end_date))
