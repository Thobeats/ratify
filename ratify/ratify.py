#!/usr/bin/python3
"""A Validator Class"""

from jsonschema.exceptions import ValidationError
import re

class Ratify:

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
            raise ValidationError(str(self.__errors))
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
            "integer" : self.is_integer,
            "list" : self.is_list,
            "dict" : self.is_dict,
            "boolean" : self.is_boolean,
            "float" : self.is_float,
            "after" : self.is_after,
            "before" : self.is_before,
            "after_or_equal" : self.is_after_or_equal,
            "before_or_equal" : self.is_before_or_equal,
            "size" : self.is_size,
            "contains" : self.is_contains,
            "confirm_password" : self.is_confirm_password,
            "less_than" : self.is_less_than,
            "less_than_or_equal" : self.is_less_than_or_equal,
            "greater_than" : self.is_greater_than,
            "greater_than_or_equal" : self.is_greater_than_or_equal,
            "mimes" : self.is_mimes
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
        if isinstance(value, str):
            if len(value) < int(min):
                error = "The {} length should not be less than {}".format(key, min)
                self.__logError(key, error)
        if isinstance(value, int):
            if value < int(min):
                error = "The {} value should not be less than {}".format(key, min)
                self.__logError(key, error)

    def is_max(self, fields, key, max=20):
        """check the max length of the value"""
        value = fields[key]
        if isinstance(value, str):
            if len(value) > int(max):
                error = "The {} length should not be more than {}".format(key, max)
                self.__logError(key, error)
        if isinstance(value, int):
            if value > int(max):
                error = "The {} value should not be more than {}".format(key, max)
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

    def is_size(self, fields, key, size):
        """checks the size of the value"""
        value = fields[key]
        if isinstance(value, int):
            if value != size:
                error = "The {} field must be {}".format(key, size)
                self.__logError(key, error)
        elif isinstance(value, str):
            if len(value) != size:
                error = "The {} field must be {} characters".format(key, size)
                self.__logError(key, error)
        elif isinstance(value, list):
            if len(value) != size:
                error = "The {} field must contain {} items".format(key, size)
                self.__logError(key, error)

    def is_contains(self, fields, key, needle):
        """checks if the value contains the given value"""
        self.is_list(fields, key)
        value = fields[key]
        if needle not in value:
            error = "The {} field must contain {}".format(key, value)
            self.__logError(key, error)

    def is_confirm_password(self, fields, key, password_field):
        """checks if the value is the same as the password"""
        value = fields[key]
        if value != fields[password_field]:
            error = "The {} field must be the same as the {}".format(key, password_field)
            self.__logError(key, error)

    def is_less_than(self, fields, key, reference):
        """checks if the value is less than the reference"""
        value = fields[key]
        if value >= fields[reference]:
            error = "The {} field must be less than {}".format(key, reference)
            self.__logError(key,error)

    def is_less_than_or_equal(self, fields, key, reference):
        """checks if the value is less than or equal to the reference"""
        value = fields[key]
        if value > fields[reference]:
            error = "The {} field must be less than or equal to {}".format(key, reference)
            self.__logError(key, error)

    def is_greater_than(self, fields, key, reference):
        """checks if the value is greater than the reference"""
        value = fields[key]
        if value <= fields[reference]:
            error = "The {} field must be greater than {}".format(key, reference)
            self.__logError(key, error)

    def is_greater_than_or_equal(self, fields, key, reference):
        """checks if the value is greater than or equal to the reference"""
        value = fields[key]
        if value < fields[reference]:
            error = "The {} field must be greater than or equal to {}".format(key, reference)
            self.__logError(key, error)

    def is_mimes(self, fields, key, mimes):
        """checks the file type"""
        value = fields[key]
        if value.split(".")[1] not in mimes.split(","):
            error = "The {} field type must be of type {}".format(key, mimes)
            self.__logError(key, error)

    def is_base64(self, fields, key):
        """checks if the value is a base64 string"""
        value = fields[key]
        check = re.fullmatch("data:image/([a-zA-Z]*);base64,([^\"]*)", value)
        if not check:
            error = "The {} field must be a base64 string".format(key)
            self.__logError(key, error)

    def is_url(self, fields, key):
        """checks if the value is a valid url"""
        value = fields[key]
        check = re.fullmatch("^(http|https)://[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+", value)
        if not check:
            error = "The {} field must be a valid url".format(key)
            self.__logError(key, error)



