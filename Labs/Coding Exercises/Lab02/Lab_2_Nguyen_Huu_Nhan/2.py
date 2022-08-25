class Mathlist:
    def __init__(self, l):
        self.l = l
    def __str__(self):
        return str(self.l)
    def __add__(self, other):
        for i in range(len(self.l)):
             self.l[i] += other
        return list.l

        

list = Mathlist([1,2,3,4])
list += 2
print(list)



