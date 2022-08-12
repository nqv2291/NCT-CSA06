from unicodedata import name


class Employee:
    name = ""
    position = ""
    def __init__(self, name , positon):
        self.name = name
        self.position = positon
    def say_hi(self):
        print(f"Hi, my name is {self.name}")
    def yourposition(self):
        print(f"Im am a/an {self.position}")

John = Employee("John" , "engineer")

John.say_hi()
John.yourposition()