class rectang:
    def __init__(self, Height,Width):
        self.height = Height
        self.width = Width
        self.perimeter = (self.width + self.height) * 2
        self.area = self.width * self.height
        print(f"=> Perimeter: {self.perimeter}")
        print(f"=> Area: {self.area}")

class round:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2 * 3.14 * self.radius
        self.area = 3.14 * self.radius**2
        print(f"=> Perimeter: {self.perimeter}")
        print(f"=> Area: {self.area}")

shape = input("Shape (rectangle|circle): ")
if(shape == 'rectangle'):
    a = float(input("Height: "))
    b = float(input("Width: "))
    square = rectang(a,b)
    square
elif(shape == 'circle'):
    a = float(input("Radius:"))
    circle = round(a)
    circle
else:
    print('=> Invalid!')

