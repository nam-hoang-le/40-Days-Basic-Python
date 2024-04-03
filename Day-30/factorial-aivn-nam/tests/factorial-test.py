import pytest 
from factorial import fact 
def factorial_of_0(): 
    assert fact(0) == 1

def factorial_of_1():
    assert fact(1) == 1

def factorial_of_5():
    assert fact(5) == 120

def factorial_of_10():
    assert fact(10) == 3628800

def factorial_of_negative_number():
    with pytest.raises(ValueError):
        fact(-5)

if __name__ == '__main__':
    pytest.main()