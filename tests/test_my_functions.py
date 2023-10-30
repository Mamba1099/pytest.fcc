import pytest
import time

from source import my_functions


def test_add():
    result = my_functions.add(1, 3)

    assert result == 4


def test_divide() -> None:
    result = my_functions.divide(4, 2)

    assert result == 2


def test_multiply() -> None:
    result = my_functions.multiply(2, 3)

    assert result == 6


def test_subtract() -> None:
    result = my_functions.subtract(4, 2)

    assert result == 2


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(4, 0)


def test_add_strings() -> None:
    result = my_functions.add("Hello ", "World")

    assert result == "Hello World"


# Run the tests

# mark and parametrize
#this is giving functions a name or label
# to apply marker to  a function you the '@pytest.mark' decorator
# you can run test with a marker by using the '-m' option together with pytest
# pytest -m <marker_name>
#inorder to see markers and their available descriptions you usen the '--markers' option    


@pytest.mark.slow # this is a marker
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2