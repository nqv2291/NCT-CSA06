import datetime

class DateHandler():
  def format_date(date):
    return date.strftime("%d/%m/%Y")

  def get_days_between(date1, date2):
    return (date2-date1).days

start_time = datetime.date(2021, 1, 1)
end_time = datetime.date(2022, 1, 1)

print("Start:", DateHandler.format_date(start_time))
print("End:", DateHandler.format_date(end_time))
print("Days between:", DateHandler.get_days_between(start_time, end_time))