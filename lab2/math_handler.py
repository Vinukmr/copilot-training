# create class math_handler,
# add a methods to return factorial of a input number,
# add a function to take input two integers and return the greatest common divisor,
# add a function to generate fibonacci series for given input number,
# check if the input is not null and int datatype and log the error if not and raise exception with appropriate message

import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class MathHandler:
    def _validate_int(self, value, var_name="Input"):
        if value is None or not isinstance(value, int):
            logging.error(f"{var_name} must be a non-null integer. Got: {value} ({type(value)})")
            raise ValueError(f"{var_name} must be a non-null integer.")

    def factorial(self, n):
        self._validate_int(n, "n")
        if n < 0:
            logging.error("Factorial is not defined for negative numbers.")
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def gcd(self, a, b):
        self._validate_int(a, "a")
        self._validate_int(b, "b")
        while b:
            a, b = b, a % b
        return abs(a)

    def fibonacci(self, n):
        self._validate_int(n, "n")
        if n < 0:
            logging.error("Fibonacci is not defined for negative numbers.")
            raise ValueError("Fibonacci is not defined for negative numbers.")
        sequence = []
        a, b = 0, 1
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
        return sequence

