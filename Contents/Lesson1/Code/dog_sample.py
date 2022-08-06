class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def rolling(self):
        print(f"{self.name} is rolling on the ground")

dog_1 = Dog("Mun", 3, "husky")
dog_1.rolling()

Dog()