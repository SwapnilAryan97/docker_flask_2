"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def tuple_list():
    """Method that returns tuple list"""
    return 1, 2


def test_calculator_add_method():
    """Testing the Calculator Add"""
    # this is show using the calculator object add method

    ## Act for AAA testing
    result = Calculator.add(tuple_list())

    ## Assertion for AAA testing
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    assert Calculator.subtract(tuple_list) == -1


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    tuple_list = (1, 2)
    assert Calculator.multiply(tuple_list) == 2

def test_calculator_multiply_method():
    """Testing the Calculator Divide"""
    tuple_list = (1, 2)
    assert Calculator.divide(tuple_list) == 0.5
