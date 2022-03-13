from calculator.calculations import Addition as Add, Subtraction as Sub, Multiplication as Mul, Division as Div

class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(tuple_list):
        """ This is the addition method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Add.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtraction method"""
        calculation = Sub.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the multiplication method"""
        calculation = Mul.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def divide(tuple_list):
        """ This is the division method"""
        calculation = Div.create(tuple_list)
        return calculation.get_result()