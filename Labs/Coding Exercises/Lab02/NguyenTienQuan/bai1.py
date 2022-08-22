class Rectangle:
    def __init__(self,height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle object with height = {self.height} and width = {self.width}"

rect = Rectangle(2, 1)
print(rect)
