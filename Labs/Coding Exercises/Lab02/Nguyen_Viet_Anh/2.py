class MathList:
    def __init__(self,lst):
        self.lst = lst
    def __str__(self):
        return str(self.lst)
    def __add__(self,value):
        for i in range(len(self.lst)):
            self.lst[i] += value
        return self.lst
    def __sub__(self,value):
        for i in range(len(self.lst)):
            self.lst[i] -= value
        return self.lst

m_list= MathList([1, 2, 3, 4, 5])
print(m_list)
m_list += 2
print(m_list)
