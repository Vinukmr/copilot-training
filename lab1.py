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
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return