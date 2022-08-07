class Rectangle():
  def __init__(self, height, width):
    self.height = height
    self.width = width
  def perimeter(self):
    return 2 * (self.height + self.width)
  def area(self):
    return self.height * self.width

class Circle():
  def __init__(self, radius):
    self.radius = radius
  def perimeter(self):
    return 6.28 * radius
  def area(self):
    return 3.14 * radius * radius

shape = input('Shape (rectangle|circle): ')
if shape == 'rectangle':
  height = float(input('Height: '))
  width = float(input('Width: ')) 
  rectangle = Rectangle(height, width)
  print()
  print(f'=> Perimeter: {rectangle.perimeter()}')
  print(f'=> Area: {rectangle.area()}')
elif shape == 'circle':
  radius = float(input('Radius: '))
  circle = Circle(radius)
  print()
  print(f'=> Perimeter: {circle.perimeter()}')
  print(f'=> Area: {circle.area()}')
else:
  print()
  print('=> Invalid!')