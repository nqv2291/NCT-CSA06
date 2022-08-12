


from cmath import pi


class Rectangle:
    width = 0
    height = 0
    def __init__(self , width , height):
        self.width = width
        self.height = height
    def peri(self):
        peri = (self.width + self.height)*2
        print(f"Perimeter: {peri}")
    def area(self):
        area = (self.width*self.height)
        print(f"Area: {area}")

class Circle:
    radius = 0
    def __init__(self , radius):
        self.radius = radius
    def peri(self):
        peri = (self.radius*2*3.14)
        print(f"Perimeter: {peri}")
    def area(self):
        area = ((self.radius^2)*3.14)
        print(f"Area: {area}")

def continueyeno():
    ans = input("Type Yes to continue or No to stop: ")
    if ans == "Yes":
        ask()
    elif ans == "No":
        print("Thanks you for your time")
def ask():
    ans1 = "rectangle"
    ans2 = "circle"
    answer = input(f"shape: {ans1} or {ans2}: ")
    if answer == ans1:
        print("You have chosen rectangle")
        height = int(input("Enter height: "))
        width = int(input("Enter width: "))
        Rec = Rectangle(width , height)
        Rec.peri()
        Rec.area()
        continueyeno()
    if answer == ans2:
        print("You have chosen circle")
        Radius = int(input("Enter radiust: "))
        Cir = Circle(Radius)
        Cir.peri()
        Cir.area()
        continueyeno()

ask()
