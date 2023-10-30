import pytest

from source.shapes import Circle


class TestCircle:
    # in a class based test it comes with two functions
    # first one is setup and second one is teardown
    def setup_method(self, method):
        print(f"setting up {method}")

    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        self.circle = Circle(2)
        result = self.circle.area()
        assert result == 12.566370614359172

    def test_perimeter(self):
        self.circle = Circle(5)
        result = self.circle.perimeter()
        assert result == 31.41592653589793
