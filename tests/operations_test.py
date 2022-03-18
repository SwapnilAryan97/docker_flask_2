"""Testing the calculator operations """
from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Operations Multiply"""
    assert Multiplication.multiply(1, 1) == 1


def test_calculator_operations_divide():
    """Testing the Operations Divide"""
    assert Division.divide(8, 4) == 2


def test_calculator_operations_divide_for_zero():
    """Testing the Operations Divide"""
    assert Division.divide(1, 0) == 'Error'
