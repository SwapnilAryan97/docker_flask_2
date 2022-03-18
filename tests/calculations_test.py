"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication, Division


def tuple_list():
    """This is the tuple function for testing"""
    return 1.0, 2


def test_calculation_addition_instance():
    """Testing the Calculator Subtract"""
    calculation = Addition.create(tuple_list())
    assert isinstance(calculation, Addition)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    calculation = Subtraction.create(tuple_list())
    assert isinstance(calculation, Subtraction)


def test_calculation_multiplication_instance():
    """Testing the Calculator Subtract"""
    calculation = Multiplication.create(tuple_list())
    assert isinstance(calculation, Multiplication)


def test_calculation_division_instance():
    """Testing the Calculator Subtract"""
    calculation = Division.create(tuple_list())
    assert isinstance(calculation, Division)


def test_calculation_add_get_result_method():
    """Testing the Calculator Addition"""
    # this is show using the calculator object add method
    calculation = Addition.create(tuple_list())
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    calculation = Subtraction.create(tuple_list())
    assert calculation.get_result() == -3


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Multiplication"""
    calculation = Multiplication.create(tuple_list())
    assert calculation.get_result() == 2


def test_calculation_divide_get_result_method():
    """Testing the Calculator Division"""
    calculation = Division.create(tuple_list())
    assert calculation.get_result() == 0.5
