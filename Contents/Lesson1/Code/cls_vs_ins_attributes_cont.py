class Student:
    """ Class representing student in NCT-CSA06"""

    std_number = 0 # Create new class attribute
    class_name = "NCT-CSA06"

    def __init__(self, name):
        """ Student fullname """
        self.name = name

        Student.std_number += 1 # increase total number of students by 1
        self.num = Student.std_number # Assign student position

    def say_hi(self):
        """ Say hi to this student """
        return "Hi " + self.name + " from " + self.class_name


print("Total: " + str(Student.std_number))
std_1 = Student("Viet")
std_2 = Student("Viet")
std_3 = Student("Viet")

print("Total: " + str(Student.std_number))
print("std_1 is at number " + str(std_1.num))
print("std_2 is at number " + str(std_2.num))
print("std_3 is at number " + str(std_3.num))

print(Student.class_name)
