import math


class Shapes:
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shapes):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shapes):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return self.width == other.width and self.length == other.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2
    

# super is used to call the parent class of the constructor 'Rectangle'
#super().__init(side_length, side_length) it passes side_lenght as both the width and length when initializing a 'Rectangle' object
# by using super you re-use the 'Rectangle' class constructor ensuring that the square is always a rectangle with equal sides

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)