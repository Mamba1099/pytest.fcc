import pytest


from source.shapes import Rectangle


# using fixtures
@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)



@pytest.fixture
def  wierd_rectangle():
    return Rectangle(5, 6)


def test_area(my_rectangle):
    assert my_rectangle.area() == (10 * 20)
   
    
def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == ((10 + 20) * 2)


def test_not_equal(my_rectangle, wierd_rectangle):
    assert my_rectangle != wierd_rectangle  # this will pass
