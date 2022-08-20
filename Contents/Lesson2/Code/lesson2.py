
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def get_distance(self, other):
#         return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __add__(self, other):
#         return "Ket qua la 1 string hehe"

#     def __len__(self):
#         return 123



# p1 = Point(0, 3)
# p2 = Point(4, 0)

# print(p1)
# print(p2)
# print(f"Distance between {p1} and {p2} is: {p1.get_distance(p2)}")

# p3 = p1 + p2
# print("len(p3) =", len(p1))


# class Person:

#     def say_hi(self):
#         print("from person")

#     def __str__(self):
#         return "person"

# class Teacher:

#     def teach_something(self):
#         print("I am teaching CS")

#     def say_hi(self):
#         print("from teacher")

    

# class SeniorTeacher(Person, Teacher):
#     pass

# st1 = SeniorTeacher()
# st1.say_hi()


# class Car:

#     def __init__(self, name, brand, year):
#         self.name = name
#         self.brand = brand
#         self._year = year
#         self.__engine = "Something private"
#         self.__cal()

#     def __cal(self):
#         return 2022 - self._year

#     def start(self):
#         return f"trigger {self.__engine},gooooooo"

# class ElectricCar(Car):

#     def cal2(self):
#         return 2025 - self._year


# camry = Car("camry", "toyota", 2020)
# tesla = ElectricCar("tesla1", "tesla", 2019)

# # print(camry.__engine)

# print(camry.start())

# print(camry.year)
# print(tesla.cal2())



class Cat:

    def __init__(self):
        self.__mood = 5
        self.__hungry = 5
        self.__energy = 5

    def __meow(self):
        print("Meowwwwwwww. GRRRRR")
    
    def sleep(self):
        self.hungry += 1
        self.energy += 1
    
    def play(self):
        self.mood += 1
        self.energy -= 1
        self.__meow()

    def feed(self):
        self.mood += 1
        self.hungry -= 1
        self.__meow()

    @property
    def mood(self):
        return self.__mood
    
    @mood.setter
    def mood(self, new_mood):
        if new_mood <= 10 and new_mood > 0:
            self.__mood = new_mood
        else:
            print("Noo wayyyyyy")       

    


bong = Cat()

bong.mood = 300

print(bong.mood)
# bong.feed()
# bong.feed()
# print(bong.mood, bong.energy, bong.hungry)


