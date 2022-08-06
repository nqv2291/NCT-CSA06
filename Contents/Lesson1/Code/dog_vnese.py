class Dog():
    """A simple attempt to model a dog."""

    # Tạo một phương thức đặc biệt (special method) tên là __init__
    # Phương thức này sẽ tự động chạy đầu tiên mỗi khi ta tạo 1 object thuộc kiểu Dog(). 
    # Ví dụ: dog_1 = Dog("lulu", 2) -> Chương trình sẽ gọi __init__(self, name, age) và nhận các giá trị:
    # +) name = "lulu"
    # +) age = 2
    # Lưu ý name, age ở đây là các tham số truyền vào hàm, KHÔNG PHẢI là các thuộc tính!!
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        # +) __init__() luôn phải có self là tham số đầu tiên, sau đó rồi ta mới cho thêm các tham số khác 
        # tùy vào trường hợp. Ở đây các tham số khác đó là name và age.
        # +) self ở đây chính là cái object vừa tạo. Nếu ta tạo dog_1 = Dog() thì self chính là dog_1
        # +) Tác dụng của self: self sẽ dùng để truy cập vào các thuộc tính (attributes) và gọi các phương thức (methods)

        # +) Đặc điểm của self: mọi biến mà có "self." đứng trước thì đều có thể truy cập được
        # từ bất cứ phương thức (method) nào khác ở trong class này.
        # Ví dụ: Bạn có thể nhìn ở method sit() ở dưới để thấy rằng ta dùng self.name để lấy được
        # thuộc tính name đã tạo trong __init__().

        self.name = name # name ở bên phải chỉ là tham số thôi (nó lấy từ đây: __init__(self, name, age)), name ở bên trái (đứng đằng sau self.) là một thuộc tính của class Dog
        self.age = age # Tương tự, age ở bên phải dấu = là tham số, age ở bên trái là một thuộc tính
        
    # Đây là phương thức sit(). Về cơ bản thì nó cũng chỉ là 1 hàm mà thôi! Tuy nhiên chỉ có object nào thuộc kiểu Dog() thì mới dùng được hàm này
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6) 
# Sau khi gõ như này, phương thức __init__() sẽ được gọi. Nó sẽ gán giá trị cho các tham số name = 'willie' và age = 6
# Lưu ý ở đây chỉ có 2 tham số được truyền, mà lúc định nghĩa __init__() ở trên ta có 3 tham số lận (self, name, age)
# là bởi vì Python đã truyền giá trị của self là my_dog. Tức là bên cạnh name = 'willie', age = 6 thì self = my_dog

# tương tự, tạo 1 object khác tên là your_dog
your_dog = Dog('Lucy', 3)


# Thử nghịch 1 chút với object có kiểu là Dog():
for dog in [my_dog, your_dog]:
    print(f"My dog's name is {dog.name}.") # truy cập vào thuộc tính name bằng cách: <tên obj>.name
    print(f"My dog is {dog.age} years old.") # truy cập vào thuộc tính age
    dog.sit() # gọi phương thức sit()
    print()