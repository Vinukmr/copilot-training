# create a class string_handler,
# add function to revert a string and return it,
# add a function to check if a string is palindrome return true if it is palindrome else false, 
# add a functin to check number of vowels in a string and return the count,
# add a function to return a string in Title case,
# all null checks for all methods and string type checks on the input string and log error message if not satisfied with these coditions and raise exception.
class StringHandler:
    def revert_string(self, s):
        """
        Reverts the input string and returns it.
        """
        if s is None:
            raise ValueError("Input cannot be None")
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return s[::-1]

    def is_palindrome(self, s):
        """
        Checks if the input string is a palindrome.
        """
        if s is None:
            raise ValueError("Input cannot be None")
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]

    def count_vowels(self, s):
        """
        Counts the number of vowels in the input string.
        """
        if s is None:
            raise ValueError("Input cannot be None")
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        vowels = "aeiouAEIOU"
        return sum(1 for c in s if c in vowels)

    def to_title_case(self, s):
        """
        Converts the input string to title case.
        """
        if s is None:
            raise ValueError("Input cannot be None")
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return s.title()