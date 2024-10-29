import unittest
from ratify.ratify import Ratify
from jsonschema.exceptions import ValidationError



class TestRatify(unittest.TestCase):
    """Tests for ratify."""

    def test_required_with_no_value(self):
        """Test the required validator."""
        data = {'name': ''}
        rule = {'name': ['required']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_required_with_value(self):
        """Test the required validator"""
        data = {'name': 'Jones'}
        rule = {'name': ['required']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_email_with_invalid_email(self):
        """Test the email validator"""
        data = {"email": "test"}
        rule = {"email": ['required', 'email']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_email_with_valid_email(self):
        """Test the email validator"""
        data = {"email": "test@test.com"}
        rule = {"email": ['required', 'email']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_min_with_string(self):
        """Test the min vallidator"""
        data = {"age": 10}
        rule = {"age": ['required', 'min:18']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_min_with_integer(self):
        """Test the min vallidator"""
        data = {"password": "testing"}
        rule = {"password": ['required', 'min:8']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_max_with_string(self):
        """Test the min vallidator"""
        data = {"age": 18}
        rule = {"age": ['required', 'max:10']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_max_with_integer(self):
        """Test the min vallidator"""
        data = {"password": "testing"}
        rule = {"password": ['required', 'max:5']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_string_with_integer(self):
        """Test the string validator"""
        data = {"name": 10}
        rule = {"name": ['required', 'string']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_string_with_string(self):
        """Test the string validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'string']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_integer_with_string(self):
        """Test the integer validator"""
        data = {"age": "Nine"}
        rule = {"age": ['required', 'integer']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_integer_with_integer(self):
        """Test the string validator"""
        data = {"age": 9}
        rule = {"age": ['required', 'integer']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_list_with_string(self):
        """Test the list validator"""
        data = {"skills": "Python"}
        rule = {"skills": ['required', 'list']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_list_with_list(self):
        """Test the list validator"""
        data = {"skills": ["Python"]}
        rule = {"skills": ['required', 'list']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertIn("Python", result['skills'])

    def test_dict_with_string(self):
        """Test the list validator"""
        data = {"skills": "Python"}
        rule = {"skills": ['required', 'dict']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_dict_with_dict(self):
        """Test the list validator"""
        data = {"skills": {"Python": "Intermediate"}}
        rule = {"skills": ['required', 'dict']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertIn("Intermediate", result['skills']['Python'])

    def test_boolean_with_string(self):
        """Test the boolean validator"""
        data = {"is_bool": "String"}
        rule = {"is_bool": ['required', 'boolean']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_boolean_with_boolean(self):
        """Test the boolean validator"""
        data = {"is_bool": True}
        rule = {"is_bool": ['required', 'boolean']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertTrue(result['is_bool'])

    def test_float_with_integer(self):
        """Test the float validator"""
        data = {"price": 20}
        rule = {"price": ['required', 'float']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_float_with_float(self):
        """Test the float validator"""
        data = {"price": 20.0}
        rule = {"price": ['required', 'float']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertEqual(20.0, result['price'])

    def test_date_with_wrong_date(self):
        """Test the date validator"""
        data = {"dob": "20-10-1990"}
        rule = {"dob": ['required', 'date']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_date_with_right_date(self):
        """Test the date validator"""
        data = {"dob": "1990-10-20"}
        rule = {"dob": ['required', 'date']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_datetime_with_wrong_datetime(self):
        """Test the datetime validator"""
        data = {"dob": "20-10-1990 10:00:00"}
        rule = {"dob": ['required', 'datetime']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_datetime_with_right_datetime(self):
        """Test the datetime validator"""
        data = {"dob": "1990-10-20 10:00:00"}
        rule = {"dob": ['required', 'datetime']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_date_format_with_the_wrong_format(self):
        """Test the date_format validator"""
        data = {"dob": "1990-10-20"}
        rule = {"dob": ['required', 'date_format:%d-%m-%Y']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_date_format_with_the_right_format(self):
        """Test the date_format validator"""
        data = {"dob": "20-10-1990"}
        rule = {"dob": ['required', 'date_format:%d-%m-%Y']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_if_date_is_after_a_given_date(self):
        """Test the after validator"""
        data = {"dob": "1990-10-20"}
        rule = {"dob": ['required', 'after:1990-10-21']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_if_date_is_before_a_given_date(self):
        """Test the before validator"""
        data = {"dob": "1990-10-21"}
        rule = {"dob": ['required', 'before:1990-10-20']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_if_date_is_after_or_equal_a_given_date(self):
        """Test the after_or_equal validator"""
        data = {"dob": "1990-10-20"}
        rule = {"dob": ['required', 'after_or_equal:1990-10-21']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_if_date_is_before_or_equal_a_given_date(self):
        """Test the before_or_equal validator"""
        data = {"dob": "1990-10-21"}
        rule = {"dob": ['required', 'before_or_equal:1990-10-20']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_size_with_string_(self):
        """Test the size validator"""
        data = {"name": "Joness"}
        rule = {"name": ['required', 'size:5']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_size_with_string(self):
        """Test the size validator"""
        data = {"name": "Joness"}
        rule = {"name": ['required', 'size:6']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_size_with_integer_(self):
        """Test the size validator"""
        data = {"age": 10}
        rule = {"age": ['required', 'size:5']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_size_with_integer(self):
        """Test the size validator"""
        data = {"age": 6}
        rule = {"age": ['required', 'size:6']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_size_with_list_(self):
        """Test the size validator"""
        data = {"ages": [10, 20, 30, 13]}
        rule = {"ages": ['required', 'size:5']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_size_with_list(self):
        """Test the size validator"""
        data = {"ages": [10, 20, 30, 13]}
        rule = {"ages": ['required', 'size:4']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_if_a_list_contains_a_value(self):
        """Test the in validator"""
        data = {"ages": [10, 20, 30, 13]}
        rule = {"ages": ['required', 'contains:14']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_if_a_list_contains_a_value_(self):
        """Test the in validator"""
        data = {"ages": [10, 20, 30, 13]}
        rule = {"ages": ['required', 'contains:10']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_confirm_password_with_wrong_password(self):
        """Test the confirm validator"""
        data = {"password": "testing", "confirm_password": "test"}
        rule = {"confirm_password": ['required', 'confirm_password:password']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_confirm_password_with_right_password(self):
        """Test the confirm validator"""
        data = {"password": "testing", "confirm_password": "testing"}
        rule = {"confirm_password": ['required', 'confirm_password:password']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_confirm_password_with_no_password(self):
        """Test the confirm validator"""
        data = {"confirm_password": "testing"}
        rule = {"confirm_password": ['required', 'confirm_password:password']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_less_than(self):
        """Test the less_than validator"""
        data = {"age": 20, "limit": 18}
        rule = {"age": ['required', 'less_than:limit']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_less_than_(self):
        """Test the less_than validator"""
        data = {"age": 18, "limit": 20}
        rule = {"age": ['required', 'less_than:limit']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_less_than_or_equal(self):
        """Test the less_than_or_equal validator"""
        data = {"age": 20, "limit": 18}
        rule = {"age": ['required', 'less_than_or_equal:limit']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_less_than_or_equal_(self):
        """Test the less_than_or_equal validator"""
        data = {"age": 20, "limit": 20}
        rule = {"age": ['required', 'less_than_or_equal:limit']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_greater_than(self):
        """Test the greater_than validator"""
        data = {"age": 18, "limit": 20}
        rule = {"age": ['required', 'greater_than:limit']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_greater_than_(self):
        """Test the greater_than validator"""
        data = {"age": 20, "limit": 18}
        rule = {"age": ['required', 'greater_than:limit']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_greater_than_or_equal(self):
        """Test the greater_than_or_equal validator"""
        data = {"age": 18, "limit": 20}
        rule = {"age": ['required', 'greater_than_or_equal:limit']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_greater_than_or_equal_(self):
        """Test the greater_than_or_equal validator"""
        data = {"age": 20, "limit": 20}
        rule = {"age": ['required', 'greater_than_or_equal:limit']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_ends_with(self):
        """Test the ends_with validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'ends_with:ss']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_ends_with_(self):
        """Test the ends_with validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'ends_with:es']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_starts_with(self):
        """Test the starts_with validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'starts_with:Mo']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_starts_with_(self):
        """Test the starts_with validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'starts_with:Jo']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_in(self):
        """Test the in validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'in:Joness,Mo']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_in_(self):
        """Test the in validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'in:Jones,Mo']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)

    def test_is_not_in(self):
        """Test the not_in validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'not_in:Jones,Mo']}
        ratify = Ratify()
        self.assertRaises(ValidationError, ratify.make, data, rule)

    def test_is_not_in_(self):
        """Test the not_in validator"""
        data = {"name": "Jones"}
        rule = {"name": ['required', 'not_in:Joness,Mo']}
        ratify = Ratify()
        result = ratify.make(data, rule)
        self.assertDictEqual(data, result)


if __name__ == '__main__':
    unittest.main()
