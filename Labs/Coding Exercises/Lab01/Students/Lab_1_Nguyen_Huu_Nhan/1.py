class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def say_hi(self):
        print(f"Hi, my name is {self.name}")
    def tell_position(self):
        print(f"I am a {self.job}")
john = Employee("John", "Software Engineer")
john.say_hi()
john.tell_position()