# create a calculator class with below methods
# create an addition method to add to integers check if they are integerns or not
# create a subsctraction method and check the largest of input integers and return the difference from largest to smallest,
# create a multiplication function with two input integers and return thier product
# create a method to divide two integers with larget integer divided by  raise exeption if divisor is zero
# create a method to power the base input with exponent input 
# create a methodd and return the factorial of the input int
# create a bool method to check if a number is prime or not
# add null checks for all methods and raise exception is input is null or not an integer type

class Calculator:
    def add(self, a, b):
        """
        Adds two integers and returns the result.

        Parameters:
            a (int): The first integer to add. Must not be None.
            b (int): The second integer to add. Must not be None.

        Returns:
            int: The sum of a and b.

        Raises:
            ValueError: If either a or b is None.
            TypeError: If either a or b is not an integer.
        """
        if a is None or b is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must be integers")
        return a + b

    def subtract(self, a, b):
        if a is None or b is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must be integers")
        return abs(a - b)

    def multiply(self, a, b):
        if a is None or b is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must be integers")
        return a * b

    def divide(self, a, b):
        if a is None or b is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must be integers")
        if b == 0:
            raise ZeroDivisionError("Divisor cannot be zero")
        return a / b

    def power(self, base, exponent):
        if base is None or exponent is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(base, int) or not isinstance(exponent, int):
            raise TypeError("Inputs must be integers")
        return base ** exponent

    def factorial(self, n):
        if n is None:
            raise ValueError("Input cannot be None")
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def is_prime(self, n):
        if n is None:
            raise ValueError("Input cannot be None")
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
# also add test cases for each method in the calculator class
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        with self.assertRaises(ValueError):
            self.calc.add(None, 3)
        with self.assertRaises(TypeError):
            self.calc.add(2, "3")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), 2)
        with self.assertRaises(ValueError):
            self.calc.subtract(None, 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(2, "3")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        with self.assertRaises(ValueError):
            self.calc.multiply(None, 3)
        with self.assertRaises(TypeError):
            self.calc.multiply(2, "3")

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(None, 3)
        with self.assertRaises(TypeError):
            self.calc.divide(2, "3")
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(2, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        with self.assertRaises(ValueError):
            self.calc.power(None, 3)
        with self.assertRaises(TypeError):
            self.calc.power(2, "3")

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(None)
        with self.assertRaises(TypeError):
            self.calc.factorial("5")

    def test_is_prime(self):
        self.assertTrue(self.calc.is_prime(5))
        self.assertFalse(self.calc.is_prime(4))
        with self.assertRaises(ValueError):
            self.calc.is_prime(None)
        with self.assertRaises(TypeError):
            self.calc.is_prime("5")

if __name__ == '__main__':
    unittest.main()
