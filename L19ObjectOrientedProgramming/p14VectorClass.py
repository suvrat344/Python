# A vector in 2D space corresponding to the point P(x,y) has one end at the origin and the other end at the point P. We are interested in the following operations on a vector:
# Scaling
# A vector can be scaled by a number s. For example, if [x,y] is a vector, then scaling it by s transforms it into the vector [s.x,s.y].
# Reflection
# If a vector [x,y] is reflected about the Y-axis, it becomes the vector [−x,y]. Likewise, if it is reflected about the X-axis, it becomes the vector [x,−y].
# Addition
# Two vectors [a,b] and [c,d] can be added to give the vector [a+c,b+d].
# Write a class named Vector that has the following specification:
# Attributes
# (1) x: int, first coordinate of the vector
# (2) y: int, second coordinate of the vector
# Methods
# (1) __init__: constructor with two arguments — x and y; assign these two values to the attributes within the constructor
# (2) print_info: print a string that represents the coordinates of the current vector in the following form: (x,y); there should be no spaces anywhere in the string; you have to print and not return the string in this case
# (3) scale: accept an integer s as argument and scale the current vector by s units
# (4) reflect_about_X: reflect the current vector about the X-axis
# (5) reflect_about_Y: reflect the current vector about the Y-axis
# (6) add: accept another Vector as argument, and return the sum of the current vector (self) and this argument; you must return an object of type Vector
# (1) Each test case corresponds to one or more method calls. We will use V to denote the name of the object.
# Input                                      Expected Output
# Test Case1
# Vector(3, 4)                                   (3,4)
# V.print_info()
# Test Case2
# Vector(4, 7)                                   (12,21)
# V.scale(3)
# V.print_info()
# Test Case3
# Vector(5, 2)                                   (8,6)
# V.add(Vector(3, 4)).print_info()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_about_X(self):
        self.y *= -1

    def reflect_about_Y(self):
        self.x *= -1

    def scale(self, s):
        self.x, self.y = s * self.x, s * self.y

    def add(self, V):
        v = Vector(0, 0)
        v.x = self.x + V.x
        v.y = self.y + V.y
        return v

    def print_info(self):
        print(f'({self.x},{self.y})')
        
    def reflect_about_Y(self):
        self.x = -1 * self.x
        
    def add(self,V):
        v = Vector(self.x+V.x,self.y+V.y)
        return v
      
      
v = Vector(3, 4)                                   
v.print_info()
v.scale(3)
v.print_info()
new_vector = v.add(Vector(3, 4))
print(new_vector.x,new_vector.y)