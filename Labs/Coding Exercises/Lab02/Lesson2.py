
#Bài 1
from datetime import datetime


class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width
  
  def __str__(self):
    return f'Rectangle object with height = {self.height} and width = {self.width}'

rect = Rectangle(2, 1)
print(rect)

#Bài 2
class MathList:
    def __init__ (self, mylist):
        self.mylist=mylist
    def __str__ (self):
        return str(self.mylist)
    def __add__ (self,a):
        new_list=[]
        for i in self.mylist:
            new_list.append(i+a)
        return MathList(new_list)
    def __sub__ (self,a):
        new_list=[]
        for i in self.mylist:
            new_list.append(i-a)
        return MathList(new_list)

m_list = MathList([1, 2, 3, 4, 5]) 
print(m_list)

m_list += 2
print(m_list)

#Bài 3:
class Square:
    def __init__ (self,side):
        self.side= side
    def cal_area(self):
        return self.side**2
class Cube(Square):
    def cal_area(self):
        return super().cal_area()*6
    def cal_volume(self):
        return self.side**3
square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())

#Bài 4
from datetime import datetime
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def welcome(self):
        print( f'Welcome, {self.username}')
    def check_password(self,input):
        if input==self.password:
            return True
        else:
            return False
class SubscribedUser(User):
    def __init__(self, username, password,expired_date):
        super().__init__(username, password)
        self.expired_date= expired_date
    def is_expired(self):
        return datetime.now() >self.expired_date
user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))
s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())