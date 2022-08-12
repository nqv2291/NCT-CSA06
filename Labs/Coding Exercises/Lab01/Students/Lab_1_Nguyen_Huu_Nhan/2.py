class Rectangle:
    def __init__(self, h, w):
        self.h = int(h)
        self.w = int(w)
    def perimeter(self):
        a = (self.h+self.w)*2
        print (f"Perimeter: {a}")
    def area(self):
        a = self.h*self.w
        print (f"Area: {a}")
class Circle:
    def __init__(self, r):
        self.r = int(r)
    def perimeter(self):
        a = self.r*2*3.14
        print (f"Perimeter: {a}")
    def area(self):
        a = self.r*self.r*3.14
        print (f"Area: {a}")
Shape = input("Shape (rectangle|circle):")
if Shape == "rectangle":
    b = input("Height: ")
    c = input("Width: ")
    obj = Rectangle(b,c)
    obj.perimeter()
    obj.area() 
elif Shape == "circle":
    b = input("Radius:")
    obj = Circle(b)
    obj.perimeter()
    obj.area() 
else:
    print("Invalid!")