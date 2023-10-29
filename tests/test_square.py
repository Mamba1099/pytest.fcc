import pytest

from my_package.source import shapes

class TestSquare:
    def setup_method(self, method):
        print(f"setting up {method}")
        
    def teardown_method(self, method):      
        print(f"tearing down {method}") 
        
    def test_area(self):
        self.square = shapes.Square(2)
        result = self.square.area()
        assert result == 4
        
    def test_perimeter(self):
        self.square = shapes.Square(5)
        result = self.square.perimeter()
        assert result == 20