# A class named Shape is given to you as a part of the prefix code. Write a class named Square that is derived from Shape with the following specification:
# Attributes
# Only those attributes that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.
# side: int, side of the square
# Methods
# Only those methods that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.
# (1) __init__: accept side as an argument:
# (2) Call the constructor of the base class and set the name attribute to "Square" using it.
# (3) Assign side to the corresponding attribute of this class.
# (4) Call the methods compute_area and compute_perimeter within the constructor.
# (5) compute_area: compute the area of the square and assign it to the attribute area.
# (6) compute_perimeter: compute the perimeter of the square and assign it to the attribute perimeter.
# (1) Each test case corresponds to one or more method calls. We will use S to denote the name of the object.
# Input                           Expected Output
# Test Case1
# Square(4)                             4
#                      Square has an area of 16 and perimeter of 16
# Test Case2
# Square(5)                             5
#                      Square has an area of 25 and perimeter of 20

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')
        
class Square(Shape):
    def __init__(self, side):
        super().__init__('Square')
        self.side = side
        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        self.area = self.side ** 2

    def compute_perimeter(self):
        self.perimeter = 4 * self.side
        
square = Square(4)
square.compute_area()
square.compute_perimeter()
square.display()