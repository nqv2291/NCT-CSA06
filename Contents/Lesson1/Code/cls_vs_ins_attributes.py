class Student:
    """ Class representing student in HDT-CSA08"""

    # Class attribute: class_name
    class_name = "HDT-CSA08"

    def __init__(self, name):
        """ Student fullname """
        # Instance attribute: name
        self.name = name
    
    def say_hi(self):
        """ Say hi to this student """
        return "Hi " + self.name + " from " + self.class_name


std_1 = Student("Viet")
print("Instance attribute:                   name = " + std_1.name)
print("Class attribute:                      class_name = " + Student.class_name)

# class attribute can be accessed by self.attribute where self is the instance itself
print("Access class attribute from instance: class_name = " + std_1.class_name) 