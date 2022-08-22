class Square:
    
    def __init__(self, length):
        self.length = length
    
    def cal_area(self):
        return self.length**2

square = Square(2)
print('Square area:',square.cal_area())

class Cube(Square):

    def __init__(self,length):
        Square.__init__(self,length)

    def cal_area(self):
        return self.length**2*6

    def cal_volume(self):
        return self.length**3

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())
