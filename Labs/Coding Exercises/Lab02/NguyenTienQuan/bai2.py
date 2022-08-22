class MathList:
    
    def __init__(self, numchain):
        self.numchain = numchain
    
    def __str__(self):
        return str(self.numchain)

    def __add__(self, value):
        for i in range(0, len(self.numchain)):
            self.numchain[i]+=value
        return self.numchain
    
    def __subb__(self, value):
        for i in range(0, len(self.numchain)):
            self.numchain[i]-=value
        return self.numchain

m_list = MathList([1, 2, 3, 4, 5])
print(m_list)

m_list+=2
print(m_list)