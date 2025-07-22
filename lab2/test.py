# create test cases for functions in validate_handler.py, math_handler.py, datetime_handler.py, string_handler.py
import unittest
from datetime import datetime
from lab2.validate_handler import ValidationHandler
from lab2.math_handler import MathHandler
from lab2.datetime_handler import DateTimeHandler
from lab2.string_handler import StringHandler
class TestValidationHandler(unittest.TestCase):
    def setUp(self):
        self.validator = ValidationHandler()

    def test_is_valid_email(self):
        self.assertTrue(self.validator.is_valid_email("test@example.com"))
        self.assertFalse(self.validator.is_valid_email("invalid-email"))

    def test_is_valid_indian_phone_number(self):
        self.assertTrue(self.validator.is_valid_indian_phone_number("+919876543210"))
        self.assertFalse(self.validator.is_valid_indian_phone_number("9876543210"))

    def test_check_password_strength(self):
        self.assertEqual(self.validator.check_password_strength("WeakPass"), "Weak")
        self.assertEqual(self.validator.check_password_strength("Medium1@"), "Medium")
        self.assertEqual(self.validator.check_password_strength("Strong Pass1@"), "Strong")

    def test_contains_special_characters(self):
        self.assertTrue(self.validator.contains_special_characters("Hello@World"))
        self.assertFalse(self.validator.contains_special_characters("HelloWorld"))


class TestMathHandler(unittest.TestCase):
    def setUp(self):
        self.math_handler = MathHandler()
    def test_factorial(self):
        self.assertEqual(self.math_handler.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.math_handler.factorial(-1)
    def test_gcd(self):
        self.assertEqual(self.math_handler.gcd(48, 18), 6)
        self.assertEqual(self.math_handler.gcd(100, 10), 10)
        self.assertEqual(self.math_handler.gcd(7, 3), 1)
    def test_fibonacci(self):
        self.assertEqual(self.math_handler.fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(self.math_handler.fibonacci(0), [])
        with self.assertRaises(ValueError):
            self.math_handler.fibonacci(-1)

class TestDateTimeHandler(unittest.TestCase):
    def setUp(self):
        self.date_time_handler = DateTimeHandler()

    def test_age_from_dob(self):
        dob = datetime(2000, 1, 1)
        age = self.date_time_handler.age_from_dob(dob)
        self.assertTrue(age >= 0)

    def test_days_between_dates(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        days = self.date_time_handler.days_between_dates(start_date, end_date)
        self.assertEqual(days, 364)

    def test_is_leap_year(self):
        self.assertTrue(self.date_time_handler.is_leap_year(2020))
        self.assertFalse(self.date_time_handler.is_leap_year(2021))

    def test_print_date_formats(self):
        date = datetime(2023, 10, 1)
        self.date_time_handler.print_date_formats(date)
    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.date_time_handler._validate_datetime(None, "Date")
        with self.assertRaises(ValueError):
            self.date_time_handler._validate_year(None)
class TestStringHandler(unittest.TestCase):
    def setUp(self):
        self.string_handler = StringHandler()

    def test_revert_string(self):
        self.assertEqual(self.string_handler.revert_string("hello"), "olleh")
        with self.assertRaises(ValueError):
            self.string_handler.revert_string(None)
        with self.assertRaises(TypeError):
            self.string_handler.revert_string(123)

    def test_is_palindrome(self):
        self.assertTrue(self.string_handler.is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(self.string_handler.is_palindrome("Hello World"))
        with self.assertRaises(ValueError):
            self.string_handler.is_palindrome(None)
        with self.assertRaises(TypeError):
            self.string_handler.is_palindrome(123)
    def test_count_vowels(self):
        self.assertEqual(self.string_handler.count_vowels("hello"), 2)
        self.assertEqual(self.string_handler.count_vowels("sky"), 0)
        with self.assertRaises(ValueError):
            self.string_handler.count_vowels(None)
        with self.assertRaises(TypeError):
            self.string_handler.count_vowels(123)
    def test_to_title_case(self):
        self.assertEqual(self.string_handler.to_title_case("hello world"), "Hello World")
        with self.assertRaises(ValueError):
            self.string_handler.to_title_case(None)
        with self.assertRaises(TypeError):
            self.string_handler.to_title_case(123)

if __name__ == '__main__':
    unittest.main()