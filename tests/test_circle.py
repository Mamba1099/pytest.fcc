import pytest

from source.shapes import Circle


class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")

    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        circle = Circle(2)
        result = circle.area()
        assert result == pytest.approx(12.57, 0.01)

    def test_perimeter(self):
        circle = Circle(5)
        result = circle.perimeter()
        assert result == pytest.approx(31.42, 0.01)

    def test_not_same_area_rectangle(self, my_rectangle):
        circle = Circle(2)
        assert circle.area() != my_rectangle.area()