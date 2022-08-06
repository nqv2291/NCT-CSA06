# define class---------------------------------------------------
class Restaurant:

    def __init__(self, name, food):
        self.restaurant_name = name
        self.cuisine_type = food

    def describe_restaurant(self):
        print("Restaurant's name: " + self.restaurant_name)
        print("Cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        print("Opening")



#---------------------------------------------------------------
res_1 = Restaurant("MindX", "Mi xao tim cat")

# print attributes
print("Attributes: ")
print(res_1.restaurant_name)
print(res_1.cuisine_type)

# invoke methods
print("\nMethods:")
res_1.describe_restaurant()
res_1.open_restaurant()

res_2 = Restaurant("Nha hang cua Viet", "Pho")