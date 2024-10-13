#!/usr/bin/python3
"""A Validator Class"""

from jsonschema.exceptions import ValidationError
import re

class Validator:

    def __init__(self) -> None:
        self.__errors:dict = dict()

    def make(self, fields, rules):
        self.__errors = dict()
        """creates a new validation request"""
        for key, value in rules.items():
            for val in value:
                # check if val has ':'
                if ":" in val:
                    vals = val.rsplit(":")
                    self.call_functions()[vals[0]](fields, key, vals[1])
                else:
                    self.call_functions()[val](fields, key)
        if len(self.__errors) > 0:
            raise ValidationError(self.__errors)
        else:
            return fields
                
    def call_functions(self):
        """maps rules to functions"""
        map = {
            "required" : self.is_required,
            "email" : self.is_email,
            "min" : self.is_min,
            "max" : self.is_max,
            "string" : self.is_string,
            "integer" : self.is_integer
        }
        return map


    def is_required(self, fields, key)->None:
        """Validates if a field is required"""
        value = fields[key]
        if value is None or value == '':
            error = "The {} field is required".format(key)
            self.__logError(key, error)
        
    def is_email(self, fields, key)->None:
        """checks if the field is a valid email"""
        value = fields[key]
        check = re.fullmatch("^[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", value)
        if not check:
            error = "This is an invalid email"
            self.__logError(key, error)

    def is_min(self, fields, key, min=3):
        """check the min length of the value"""
        value = fields[key]
        if len(value) < int(min):
            error = "The {} length should not be less than {}".format(key, min)
            self.__logError(key, error)


    def is_max(self, fields, key, max=20):
        """check the max length of the value"""
        value = fields[key]
        if len(value) > int(max):
            error = "The {} length should not be more than {}".format(key, max)
            self.__logError(key, error)
        
    def __logError(self, key, error):
        """logs the validation errors"""
        if key in self.__errors:
            self.__errors[key].append(error)
        else:
            self.__errors[key] = []
            self.__errors[key].append(error)

    def is_string(self, fields, key):
        """checks if the field is a string"""
        value = fields[key]
        if not isinstance(value, str):
            error = "The {} field should be a string".format(key)
            self.__logError(key, error)

    def is_integer(self, fields, key):
        """checks if the field is an integer"""
        value = fields[key]
        if not isinstance(value, int):
            error = "The {} field should be an integer".format(key)
            self.__logError(key, error)

    def is_list(self, fields, key):
        """checks if the field is a list"""
        value = fields[key]
        if not isinstance(value, list):
            error = "The {} field should be a list".format(key)
            self.__logError(key, error)

    def is_dict(self, fields, key):
        """checks if the field is a dictionary"""
        value = fields[key]
        if not isinstance(value, dict):
            error = "The {} field should be a dictionary".format(key)
            self.__logError(key, error)

    def is_boolean(self, fields, key):
        """checks if the field is a boolean"""
        value = fields[key]
        if not isinstance(value, bool):
            error = "The {} field should be a boolean".format(key)
            self.__logError(key, error)

    def is_float(self, fields, key):
        """checks if the field is a float"""
        value = fields[key]
        if not isinstance(value, float):
            error = "The {} field should be a float".format(key)
            self.__logError(key, error)

    def is_after(self, fields, key, date):
        """checks if the date is after the given date"""
        value = fields[key]
        if value <= date:
            error = "The {} field should be after {}".format(key, date)
            self.__logError(key, error)

    def is_before(self, fields, key, date):
        """checks if the date is before the given date"""
        value = fields[key]
        if value >= date:
            error = "The {} field should be before {}".format(key, date)
            self.__logError(key, error)

    def is_after_or_equal(self, fields, key, date):
        """checks if the date is after or equal to the given date"""
        value = fields[key]
        if value < date:
            error = "The {} field should be after or equal to {}".format(key, date)
            self.__logError(key, error)

    def is_before_or_equal(self, fields, key, date):
        """checks if the date is before or equal to the given date"""
        value = fields[key]
        if value > date:
            error = "The {} field should be before or equal to {}".format(key, date)
            self.__logError(key, error)

    
