
class thesquare:

    def __init__(self, sidet):
        self.sidet = sidet
    def square_area(self):
        print(f"square area:{self.sidet^2}")

class thecube(thesquare):
    
    def __init__(self, sidet):
        super().__init__(sidet)
    def cube_area(self):
        print(f"cube area:{(self.sidet^2)*6 }")
    def cube_volume(self):
        print(f"cube volume:{(self.sidet^3) }")

squaree = thesquare(2)
print(squaree.square_area)
cubee = thecube(2)
print(cubee.cube_area)
print(cubee.cube_volume)
