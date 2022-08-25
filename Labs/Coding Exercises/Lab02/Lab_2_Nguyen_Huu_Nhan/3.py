class Square:
    def __init__(self, l):
        self.l = l
    def cal_area(self):
        return self.l**2
class Cube(Square):
    def __init__(self, l):
        super().__init__(l)
    def cal_area(self):
        return super().cal_area() * 6
    def cal_volume(self):
        return self.l**3 
a = Cube(2)
square = Square(2)
print('Square area:', square.cal_area())
print('Cube area:', a.cal_area())
print('Cube volume:', a.cal_volume())