
class mathlist:
    def __init__(self , list):
        self.list = list
    def __add__(self, increase):
        newlist = []
        for i in range (len(self.list)):
            newlist.append(self.list[i] + increase )  
        return mathlist(newlist) 
    def __sub__(self, decrease):
        newlist = []
        for i in range (len(self.list)):
            newlist.append(self.list[i] - decrease )    
        return mathlist(newlist) 
    def __str__(self):
        return str(self.list)
mathlise = mathlist([1,2,3,4,5,6,7,8,9])
print(mathlise)
mathlise +=2
print(mathlise)          