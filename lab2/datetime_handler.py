# create a class datetime_handler,
# add a method return the age from input date of birth,
# add a method to find the difference in days between to input datetime variables,
# add a function to check if a given year is leap year and return boolean value,
# add a function to print date in all possible formats,
# check the input datatypes, null check and error logging with appropriate exception messages
from datetime import datetime, timedelta
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class DateTimeHandler:
    def _validate_datetime(self, value, var_name="Input"):
        if value is None or not isinstance(value, datetime):
            logging.error(f"{var_name} must be a non-null datetime. Got: {value} ({type(value)})")
            raise ValueError(f"{var_name} must be a non-null datetime.")

    def _validate_year(self, year):
        if year is None or not isinstance(year, int):
            logging.error(f"Year must be a non-null integer. Got: {year} ({type(year)})")
            raise ValueError("Year must be a non-null integer.")
    def age_from_dob(self, dob):
        self._validate_datetime(dob, "Date of Birth")
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def days_between_dates(self, start_date, end_date):
        self._validate_datetime(start_date, "Start Date")
        self._validate_datetime(end_date, "End Date")
        return (end_date - start_date).days

    def is_leap_year(self, year):
        self._validate_year(year)
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def print_date_formats(self, date):
        self._validate_datetime(date, "Date")
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%B %d, %Y",
            "%m-%d-%Y %H:%M:%S"
        ]
        for fmt in formats:
            print(date.strftime(fmt))