import datetime
datetime = datetime.datetime
class User:
    def __init__(self, n, p):
        self.n = n
        self.p = p
    def welcome(self):
        print(f"Welcome, {self.n}")
    def check_password(self, other):
        if self.p == other:
            return True
        return False
class SubscribedUser(User):
    def __init__(self, n, p, d):
        super().__init__(n,p)
        self.d = d
    def is_expired(self):
        if self.d < datetime.now():
            return True
        return False
print (datetime.now().strftime("%d/%m/%Y"))
user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))
s_user = SubscribedUser('s_mindx', '1234',datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
