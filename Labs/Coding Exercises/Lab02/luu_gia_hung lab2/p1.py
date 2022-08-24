class regtangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width
    def __str__(self):
        return f"regtangle object with height = {self.height} and width = {self.width}"
    
rect = regtangle(
    int(input("enter height: ")) , 
    int(input("enter width: ")) 
)
print(rect)