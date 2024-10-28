#!/usr/bin/python3
"""A Validator Class"""

from jsonschema.exceptions import ValidationError
import re
import datetime

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
            "mimes" : self.is_mimes,
            "url" : self.is_url,
            "file": self.is_file,
            "ends_with": self.is_ends_with,
            "starts_with": self.is_starts_with,
            "in": self.is_in,
            "not_in": self.is_not_in,
            "in_array": self.is_in_array,
            "not_in_array": self.is_not_in_array,
            "alpha": self.is_alpha,
            "alpha_num": self.is_alpha_num,
            "uppercase": self.is_uppercase,
            "lowercase": self.is_lowercase,
            "same": self.is_same,
            "required_if": self.is_required_if,
            "date": self.is_date,
            "datetime": self.is_datetime,
            "date_format": self.is_date_format
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
            if value != int(size):
                error = "The {} field must be {}".format(key, size)
                self.__logError(key, error)
        elif isinstance(value, str):
            if len(value) != int(size):
                error = "The {} field must be {} characters".format(key, size)
                self.__logError(key, error)
        elif isinstance(value, list):
            if len(value) != int(size):
                error = "The {} field must contain {} items".format(key, size)
                self.__logError(key, error)

    def is_contains(self, fields, key, needle):
        """checks if the value contains the given value"""
        self.is_list(fields, key)
        value = list(map(str, fields[key]))
        if needle not in value:
            error = "The {} field must contain {}".format(key, needle)
            self.__logError(key, error)

    def is_confirm_password(self, fields, key, password_field):
        """checks if the value is the same as the password"""
        value = fields[key]
        if password_field not in fields.keys():
            error = "The {} field is missing".format(password_field)
            self.__logError(key, error)
        elif value != fields[password_field]:
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
        value = fields.files[key]
        if value.split(".")[1] not in mimes.split(","):
            error = "The {} field format is not allowed".format(key)
            self.__logError(key, error)

    def is_url(self, fields, key):
        """checks if the value is a valid url"""
        value = fields[key]
        check = re.fullmatch("^(http|https)://[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+", value)
        if not check:
            error = "The {} field must be a valid url".format(key)
            self.__logError(key, error)

    def is_file(self, fields, key, allowable_file_extensions):
        """checks if the value is a file"""
        value = fields.files[key]
        filename = value.filename
        if filename.split(".")[1] not in allowable_file_extensions.split(","):
            error = "The {} field format is not allowed".format(key)
            self.__logError(key, error)

    def is_ends_with(self, fields, key, ends_with):
        """checks if the value ends with some characters"""
        value = fields[key]
        options = ends_with.split(",")
        match = 0
        for option in options:
            if value.endswith(option):
                match += 1
        if match == 0:
            error = "The {} field must end with {}".format(key, ends_with)
            self.__logError(key, error)

    def is_starts_with(self, fields, key, starts_with):
        """checks if the value starts with some characters"""
        value = fields[key]
        options = starts_with.split(",")
        match = 0
        for option in options:
            if value.startswith(option):
                match += 1
        if match == 0:
            error = "The {} field must start with {}".format(key, starts_with)
            self.__logError(key, error)

    def is_in(self, fields, key, options):
        """checks if the value is in the options"""
        value = fields[key]
        options = options.split(",")
        if value not in options:
            error = "The {} field must be in {}".format(key, options)
            self.__logError(key, error)

    def is_not_in(self, fields, key, options):
        """checks if the value is not in the options"""
        value = fields[key]
        options = options.split(",")
        if value in options:
            error = "The {} field must not be in {}".format(key, options)
            self.__logError(key, error)

    def is_in_array(self, fields, key, array_field):
        """checks if the value is in the array"""
        value = fields[key]
        array = fields[array_field]
        if value not in array:
            error = "The {} field must be in the {} field".format(key, array_field)
            self.__logError(key, error)

    def is_not_in_array(self, fields, key, array_field):
        """checks if the value is not in the array"""
        value = fields[key]
        array = fields[array_field]
        if value in array:
            error = "The {} field must not be in the {} field".format(key, array_field)
            self.__logError(key, error)

    def is_alpha(self, fields, key):
        """checks if the value is alphabetic"""
        value = fields[key]
        if not value.isalpha():
            error = "The {} field must be alphabetic".format(key)
            self.__logError(key, error)

    def is_alpha_num(self, fields, key):
        """checks if the value is alphanumeric"""
        value = fields[key]
        if not value.isalnum():
            error = "The {} field must be alphanumeric".format(key)
            self.__logError(key, error)

    def is_uppercase(self, fields, key):
        """checks if the value is uppercase"""
        value = fields[key]
        if not value.isupper():
            error = "The {} field must be uppercase".format(key)
            self.__logError(key, error)

    def is_lowercase(self, fields, key):
        """checks if the value is lowercase"""
        value = fields[key]
        if not value.islower():
            error = "The {} field must be lowercase".format(key)
            self.__logError(key, error)

    def is_same(self, fields, key, other_field):
        """checks if the value is the same as another field"""
        value = fields[key]
        if value != fields[other_field]:
            error = "The {} field must be the same as the {} field".format(key, other_field)
            self.__logError(key, error)

    def is_required_if(self, fields, key, other_field):
        """checks if the value is required if another field is present"""
        value = fields[key]
        reference = other_field.split(",")
        reference_value = fields[reference[0]]
        reference.remove(reference[0])
        if reference_value in reference and value is None:
            error = "The {} field is required".format(key)
            self.__logError(key, error)

    def is_date(self, fields, key):
        """checks if the value is a date"""
        value = fields[key]
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            error = "The {} field must be a date".format(key)
            self.__logError(key, error)

    def is_datetime(self, fields, key):
        """checks if the value is a datetime"""
        value = fields[key]
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            error = "The {} field must be a datetime".format(key)
            self.__logError(key, error)

    def is_date_format(self, fields, key, date_format):
        """checks if the value is in the given date format"""
        value = fields[key]
        try:
            datetime.datetime.strptime(value, date_format)
        except ValueError:
            error = "The {} field must be in the {} format".format(key, date_format)
            self.__logError(key, error)
