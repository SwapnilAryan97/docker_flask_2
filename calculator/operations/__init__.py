""" These are the Operation Classes"""


class Addition:
    """This is the Addition Class"""

    @staticmethod
    def add(self, value1, value2):
        """This is the addition method"""
        return value1 + value2


class Subtraction:
    """This is the subtraction Class"""

    @staticmethod
    def subtract(self, value1, value2):
        """This is subtraction method"""
        return value1 - value2


class Multiplication:
    """This is the Multiplication Class"""

    @staticmethod
    def multiply(self, value1, value2):
        """This is multiplication method"""
        return value1 * value2


class Division:
    """This is the Divion Class"""

    @staticmethod
    def divide(self, value1, value2):
        """This is division method"""
        if value2 == 0:
            return 'Error'
        return value1 / value2
