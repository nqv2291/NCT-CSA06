from datetime import datetime

class CustomDate():
  def __init__(self):
    self.time = datetime.now()
  def get_date(self):
    return self.time.strftime("%d/%m/%Y")
  def get_time(self):
    return self.time.strftime("%H:%M:%S")

now = CustomDate()
print(now.get_date())
print(now.get_time())