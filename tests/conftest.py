import pytest

import source.shapes as shapes

# using fixtures
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)



@pytest.fixture
def  wierd_rectangle():
    return shapes.Rectangle(5, 6)
