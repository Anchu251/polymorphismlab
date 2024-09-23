#LAB:POLYMORPHISM
print ('1.EXECUTE')
#truyền hàm
def execute(func, *arg, **kwargs):
    return func(*arg, **kwargs)
def say_hello(name, my_name): 
    print(f"Hello, {name}, I am {my_name}")
def say_bye(name):
    print(f"Bye, {name}")
execute(say_hello, "Peter", "George") 
execute(say_bye, "Peter")

print('\n 2.INSTRUMENTS')
#truyền instance của 1 lớp có phương thức play
def play_instrument(instrument):
    instrument.play()
class Guitar:
    def play(self):
        print('playing the guitar')
guitar = Guitar()
play_instrument(guitar)

class Piano:
    def play(self):
        print('Playing the piano')
piano = Piano()
play_instrument(piano)

print('\n3.SHAPES')
#abstract class Shape
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius #private
    def calculate_area(self):
        return 3.14*self.__radius**2
    def calculate_perimeter(self):
        return 3.14*self.__radius*2
class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    def calculate_area(self):
        return self.__height*self.__width
    def calculate_perimeter(self):
        return 2*(self.__height+self.__width)
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10,20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

print('\n 4.IMAGE AREA')
class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width*self.height
    #magic methods : kí hiệu bằng hai dấu gạch dưới _ đầu và cuối tên pg thức
    #other: đối tượng đem ra so sánh với đối tượng self hiện tại
    def __lh__(self, other):
        return self.get_area() > other.get_area()
    
    def __lb__(self, other):
        return self.get_area() >= other.get_area()
    
    def __nh__(self, other):
        return self.get_area() < other.get_area()
    
    def __nb__(self, other):
        return self.get_area() <= other.get_area()
    
    def __bn__(self, other):
        return self.get_area() == other.get_area()
    
    def __kb__(self, other):
        return self.get_area() != other.get_area()
#test code
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
print(a1 != a2)
print(a1 >= a3)
print(a1 <= a2)
print(a1 < a3)