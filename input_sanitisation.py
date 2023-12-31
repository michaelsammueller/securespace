# Imports
from imports import re

# Input Sanitisation Service Class
class Input_Sanitisation_Service:

    def filter_sql_keywords(self, user_input):
        """Filters SQL keywords from user input"""
        sql_keywords = ['SELECT', 'UPDATE', 'INSERT', 'DELETE', 'FROM', 'WHERE', 'JOIN']
        sanitized_input = user_input

        for keyword in sql_keywords:
            sanitized_input = sanitized_input.replace(keyword, '') # Replace SQL keywords with empty string

        return sanitized_input


    def filter_special_characters(self, user_input):
        """Filters special characters from user input"""
        sanitized_input = re.sub(r'[^\w\s]', '', user_input) # Replace special characters with empty string
        return sanitized_input

    
    def assert_input_size(self, user_input, min_size, max_size):
        """Asserts that the length of input is within specified range"""
        if len(user_input) < min_size or len(user_input) > max_size:
            raise ValueError(f"Input must be between {min_size} and {max_size} characters long")
        else:
            return True

    def assert_number(self, user_input):
        """Asserts that input is a number"""
        try:
            float(user_input) # Convert input to float
        except ValueError:
            raise ValueError("Input must be a number.")

    def match_pattern(self, user_input, pattern):
        """Matches input against specified pattern"""
        match = re.match(pattern, user_input) 
        return bool(match) # Returns True if match is found, False otherwise