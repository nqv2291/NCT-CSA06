class Rec:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def __str__(self):
        return f"Rectangle object with height = {self.w} and width = {self.h}"
Rece = Rec(2,1)
print (Rece)

