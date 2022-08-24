from datetime import datetime

class user:
    def __init__(self , username , password):
        self.username = username
        self.password = password

    def welcome(self):
        print(f"hello {self.username}")
    def check(self , yourname , yourpass):
        if yourname == self.username and yourpass == self.password:
            print("welcome")
        else:
            print("incorrect password or username, please retry") 

class usersub(user):
    def __init__(self, username, password , exp_date):
        super().__init__(username, password)
        self.exp_date = exp_date
    def is_expired(self):
        return datetime.now() > self.exp_date

user1 = usersub("user1" , "12345" , datetime(2021, 1, 1))
users = input("enter your username: ")
passw = input("enter your password: ")
user1.check(users , passw)
print(user1.is_expired())