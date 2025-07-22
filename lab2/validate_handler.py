# create a class named validation handler,
# add a functino to validate if given input string is a valid email address or not,
# add a function to validate given input string is a valid indian phonenumber along with country code,
# add a functino to check strength of the password and return weak,strong or medium,
# also add condtion to include one special char,uppercase,lowercase,numerical character in the password,
# add function to validate if the given input string doesn't contain special characters, remover PII information like name, email. phone number, address
# import logger and log error messages for invalid inputs,
#in password stregth function if password container space character and satisfies all other conditions consider it as strong


import re
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class ValidationHandler:
    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            logging.error(f"Invalid email address: {email}")
            return False
        return True

    def is_valid_indian_phone_number(self, phone_number):
        phone_regex = r'^\+91[6-9]\d{9}$'
        if not re.match(phone_regex, phone_number):
            logging.error(f"Invalid Indian phone number: {phone_number}")
            return False
        return True

    def check_password_strength(self, password):
        if len(password) < 8:
            return "Weak"
        has_upper = re.search(r'[A-Z]', password)
        has_lower = re.search(r'[a-z]', password)
        has_digit = re.search(r'[0-9]', password)
        has_special = re.search(r'[@$!%*?&]', password)
        has_space = ' ' in password
        if has_upper and has_lower and has_digit and has_special:
            if has_space:
                return "Strong"
            else:
                return "Medium"
        else:
            return "Weak"

    def contains_special_characters(self, text):
        special_char_regex = r'[!@#$%^&*(),.?":{}|<>]'
        if re.search(special_char_regex, text):
            logging.error(f"Text contains special characters: {text}")
            return True
        return False

    # def remove_pii(self, text):
    #     # Remove PII information
    #     text = re.sub(r'\b[A-Z][a-z]+\b', '[NAME]', text)  # Replace names
    #     text = re.sub(r'\b\d{5}(-\d{4})?\b', '[ZIP]', text)  # Replace ZIP codes
    #     text = re.sub(r'\b\d{10}\b', '[PHONE]', text)  # Replace phone numbers
    #     text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)  # Replace emails
    #     return text