from datetime import datetime

class DateHandler:

    def format_date(date):
        return date.strftime("%d/%m/%Y")

    def get_days_between(date1, date2):
        return (date2 - date1).days


start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

print("Start:", DateHandler.format_date(start_date)) # 01/01/2021
print("End:", DateHandler.format_date(end_date))     # 01/01/2022
print("Days between:", DateHandler.get_days_between(start_date, end_date))
