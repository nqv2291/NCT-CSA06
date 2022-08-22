from datetime import date, datetime


class User:

    def __init__(self, acc, pas):
        self.acc= acc
        self.pas= pas
    
    def welcome(self):
        print("Welcome,", self.acc)

    def check_password(self, value):
        if self.pas == value:
            return("True")
        return("False")

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

class SubscribedUser(User):

    def __init__(self, acc, pas, date):
        User.__init__(self,acc,pas)
        self.date = date
    
    def is_expired(self):
        if self.date < datetime.now():
            return 'True'
        return 'False'

s_user = SubscribedUser('s_mindx', '1234', datetime(2021,1,1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())