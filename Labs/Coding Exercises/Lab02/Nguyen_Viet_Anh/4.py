from datetime import datetime

class User:
    def __init__(self,usname,psword):
        self.usname = usname
        self.psword = psword
    def welcome(self):
        print(  f"welcome, {self.usname}"  )
    def check_password(self, password):
        return password == self.psword
class SubscribedUser(User):
    def __init__(self,usname,psword,date):
        super().__init__(usname,psword)
        self.date = date
    def is_expired(self):
        return datetime.now() > self.date

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2023, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
