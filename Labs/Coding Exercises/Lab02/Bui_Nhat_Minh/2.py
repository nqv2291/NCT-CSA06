class MathList:
  def __init__(self, array):
    self.array = array
  def __add__(self, increment):
    new_arr = []
    for i in range(len(self.array)):
      new_arr.append(self.array[i] + increment)
    return MathList(new_arr)
  def __sub__(self, decrement):
    new_arr = []
    for i in range(len(self.array)):
      new_arr.append(self.array[i] - decrement)
    return MathList(new_arr)
  def __str__(self):
    return str(self.array)

m_list = MathList([1, 2, 3, 4, 5]) 
print(m_list)

m_list += 2
print(m_list)