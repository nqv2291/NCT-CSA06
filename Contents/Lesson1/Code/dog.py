class Dog():
    """A simple attempt to model a dog."""

    # define a special method
    # this one runs automatically whenever we create a new instance of class Dog
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        # self: MUST come before other parameters
        # self is a reference to the instance itself, give the instance
        # access to the attributes & methods in the class

        # Any variable with prefix "self." is available to every method in the class
        self.name = name # name (on the right) is the passed parameter, now is stored in variable 'name'
        self.age = age # these variable on the left after '.' is called attribute
        
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6) 
# method __init__() is called. It set the name, age values, then it return an obj
# that will be stored in variable my_dog

your_dog = Dog('Lucy', 3)

# practicing with Dog class
for dog in [my_dog, your_dog]:
    print(f"My dog's name is {dog.name}.")
    print(f"My dog is {dog.age} years old.")
    dog.sit()
    print()