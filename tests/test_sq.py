import pytest
import source.shapes as shapes


# with parametrize we can run multiple tests with different values
# it makes it easier to test different classes without duplicating code
@pytest.mark.parametrize("side_length, expected_area", [(2, 4),(8, 64), (5, 25), (7, 49)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area