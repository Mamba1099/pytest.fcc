import pytest

from source.shapes import Square


class TestSquare:
    def setup_method(self, method):
        print(f"setting up {method}")

    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        square = Square(2)
        result = square.area()
        assert result == 4

    def test_perimeter(self):
        square = Square(5)
        result = square.perimeter()
        assert result == 20