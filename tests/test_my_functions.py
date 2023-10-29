import pytest

from my_package.source import  my_functions

def test_add(): 
    result = my_functions.add(1, 3)
    
    assert result == 4
    
def test_divide()-> None:
    result = my_functions.divide(4, 2)

    assert result == 2
    
def test_multiply()-> None:                                        
    result = my_functions.multiply(2, 3)
    
    assert result == 6
    
def test_subtract()-> None:
    result = my_functions.subtract(4, 2)
    
    assert result == 2
    
# Run the tests