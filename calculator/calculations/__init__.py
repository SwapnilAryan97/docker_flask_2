"""Calculation add, sub, multiply, divide Classes """
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mul, Division as Div


class Calculations:
    """"Calculations abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, tuple_list: tuple):
        """Constructor method"""
        self.values = Calculations.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """standardize values to list of floats"""

        list_values = []
        for val in tuple_list:
            list_values.append(float(val))
        return tuple(list_values)


class Addition(Calculations):
    """Calculation addition class"""

    def get_result(self):
        """get the addition result"""

        res = 0
        for value in self.values:
            res = Add.add(res, value)
        return res


class Subtraction(Calculations):
    """Calculation Subtraction class"""

    def get_result(self):
        """get the Subtraction result"""

        res = 0
        for value in self.values:
            res = Sub.subtract(res, value)
        return res


class Multiplication(Calculations):
    """Calculation Multiplication class"""

    def get_result(self):
        """get the Multiplication result"""

        res = 1
        for value in self.values:
            res = Mul.multiply(res, value)
        return res


class Division(Calculations):
    """Calculation Division class"""

    def get_result(self):
        """get the Division result"""

        res = 1
        for value in self.values:
            res = Div.divide(res, value)
        return res
