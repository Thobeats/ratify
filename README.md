<h1>RATIFY </h1>

<p>Ratify is a python based validator. It can be used to validate strings, integers, floats, lists and dicts.</p>

<div class="px-4 py-12 min-h-[100vh]" id="make">
    <h2 class="text-xl font-bold mt-6">make</h2>
    <p class="text-wrap my-3">
        The make method is used to validate data against a schema. The make method takes two arguments, data and rule. The data argument is the data that you want to validate, and the rule argument is the schema that you want to validate the data against.
    </p>
    <p class="text-wrap my-3">
        The make method returns a dictionary with the validated data. If the data is invalid, the make method raises a ValidationError exception.
    </p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-2 w-full">

        from ratify.ratify import Ratify

        validator = Ratify()

        try:
            data = {
                "name": "John Doe",
                "email": "john@ratify.com",
                "age": 25
            }

            rule = {
                "name": ['required'],
                "email": ['required', 'email'],
                "age": ['required', 'integer', 'max:30']
            }

            validated = validator.make(data, rule)
        except ValidationError as e:
            print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="alpha">
    <h2 class="text-xl font-bold mt-6">alpha</h2>
    <rule>alpha</rule>

<p class="text-wrap my-3">
    The alpha rule is used to check if a field contains only alphabetic characters. If the field contains any non-alphabetic characters, the alpha rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The alpha rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "John Doe",
        }

        rule = {
            "name": ['alpha'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
                     
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="alpha_num">
<h2 class="text-xl font-bold mt-6">alpha_num</h2>
<rule>alpha_num</rule>

<p class="text-wrap my-3">
    The alpha_num rule is used to check if a field contains only alphabetic and numeric characters. If the field contains any non-alphabetic or non-numeric characters, the alpha_num rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The alpha_num rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "username": "JohnDoe657",
        }

        rule = {
            "username": ['alpha_num'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                    
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="after">
<h2 class="text-xl font-bold mt-6">after</h2>
<rule>after:date</rule>

<p class="text-wrap my-3">
    The after rule is used to check if a date is after a specified date. If the date is not after the specified date, the after rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The after rule takes one argument, date, which is the date that the field should be after. The date argument should be in the format YYYY-MM-DD.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "start": "2024-10-20",
        }

        rule = {
            "start": ['after:2024-11-01'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                   
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="after_or_equal">
<h2 class="text-xl font-bold mt-6">after_or_equal</h2>
<rule>after_or_equal:date</rule>

<p class="text-wrap my-3">
    The after_or_equal rule is used to check if a date is after or equal to a specified date. If the date is not after or equal to the specified date, the after_or_equal rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The after_or_equal rule takes one argument, date, which is the date that the field should be after or equal to. The date argument should be in the format YYYY-MM-DD.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "start_date": "2024-10-20",
        }

        rule = {
            "start_date": ['after_or_equal:2024-11-01'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                   
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="before">
<h2 class="text-xl font-bold mt-6">before</h2>
<rule>before:date</rule>

<p class="text-wrap my-3">
    The before rule is used to check if a date is before a specified date. If the date is not before the specified date, the before rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The before rule takes one argument, date, which is the date that the field should be before. The date argument should be in the format YYYY-MM-DD.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "deadline": "2024-10-20",
        }

        rule = {
            "deadline": ['after:2024-11-01'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                    
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="before_or_equal">
<h2 class="text-xl font-bold mt-6">before_or_equal</h2>
<rule>before_or_equal:date</rule>

<p class="text-wrap my-3">
    The before_or_equal rule is used to check if a date is before or equal to a specified date. If the date is not before or equal to the specified date, the before_or_equal rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The before_or_equal rule takes one argument, date, which is the date that the field should be before or equal to. The date argument should be in the format YYYY-MM-DD.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "deadline": "2024-10-20",
        }

        rule = {
            "deadline": ['before_or_equal:2024-11-01'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                    
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="boolean">
<h2 class="text-xl font-bold mt-6">boolean</h2>
<rule>boolean</rule>

<p class="text-wrap my-3">
    The boolean rule is used to check if a field is a boolean value. If the field is not a boolean value, the boolean rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The boolean rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "is_available": True
        }

        rule = {
            "is_available": ['boolean'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="confirm_password">
<h2 class="text-xl font-bold mt-6">confirm_password</h2>
<rule>confirm_password:password_field</rule>

<p class="text-wrap my-3">
    The confirm_password rule is used to check if a field matches another field. If the field does not match the other field, the confirm_password rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The confirm_password rule takes one argument, password_field, which is the field that the field should match.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "enter_password": "1234Password ",
            "confirm_password": "1234Password "
        }

        rule = {
            "confirm_password": ['confirm_password:enter_password']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="contains">
<h2 class="text-xl font-bold mt-6">contains</h2>
<rule>contains:foo</rule>

<p class="text-wrap my-3">
    The contains rule is used to check if a value exists in a list. If the list does not contain the specified value, the contains rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The contains rule takes one argument, value, which is the value that the list should contain.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "ages": [1, 2, 3, 4, 5]
        }

        rule = {
            "ages": ['contains:3']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="date">
<h2 class="text-xl font-bold mt-6">date</h2>
<rule>date</rule>

<p class="text-wrap my-3">
    The date rule is used to check if a field is a valid date. If the field is not a valid date, the date rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The date rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "start_date": "2024-10-20"
        }

        rule = {
            "start_date": ['date']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="date_format">
<h2 class="text-xl font-bold mt-6">date_format</h2>
<rule>date_format:format</rule>

<p class="text-wrap my-3">
    The date_format rule is used to check if a field is a valid date with a specified format. If the field is not a valid date with the specified format, the date_format rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The date_format rule takes one argument, format, which is the format that the date should be in. The format argument should be a valid date format string.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "start_date": "10-20-2024"
        }

        rule = {
            "start_date": ['date_format:%m-%d-%Y']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="datetime">
<h2 class="text-xl font-bold mt-6">datetime</h2>
<rule>datetime</rule>

<p class="text-wrap my-3">
    The datetime rule is used to check if a field is a valid datetime. If the field is not a valid datetime, the datetime rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The datetime rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "start_date": "2024-10-20 12:30:05"
        }

        rule = {
            "start_date": ['datetime']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                 
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="dict">
<h2 class="text-xl font-bold mt-6">dict</h2>
<rule>dict</rule>

<p class="text-wrap my-3">
    The dict rule is used to check if a field is a valid dictionary. If the field is not a valid dictionary, the dict rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The dict rule takes no argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "inventory": {"name": "John Doe", "age": 23, "country": "Nigeria"}
        }

        rule = {
            "inventory": ['dict']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="email">
<h2 class="text-xl font-bold mt-6">email</h2>
<rule>email</rule>

<p class="text-wrap my-3">
    The email rule is used to check if a field is a valid email address. If the field is not a valid email address, the email rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The email rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "email_address": "john@ratify.com",
        }

        rule = {
            "email_address": ['email'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="ends_with">
<h2 class="text-xl font-bold mt-6">ends_with</h2>
<rule>ends_with:foo</rule>

<p class="text-wrap my-3">
    The ends_with rule is used to check if a field ends with a specified value. If the field does not end with the specified value, the ends_with rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The ends_with rule takes one argument, foo, which is the value that the field should end with.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "Jones",
        }

        rule = {
            "name": ['ends_with:es'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="file">
<h2 class="text-xl font-bold mt-6">file</h2>
<rule>file:extensions</rule>

<p class="text-wrap my-3">
    The file rule checks if the file is a valid file and if the file has the specified extensions. If the file is not valid or does not have the specified extensions, the file rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The file rule takes one argument, extensions, which is a comma-separated list of file extensions that the file should have.
</p>

note: The file rule only works with the Flask file object
<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "cv": "document.pdf",
        }

        rule = {
            "cv": ['file:pdf,txt,doc'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="float">
<h2 class="text-xl font-bold mt-6">float</h2>
<rule>float</rule>

<p class="text-wrap my-3">
    The float rule is used to check if a field is a valid float. If the field is not a valid float, the float rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The float rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "price": 24.32,
        }

        rule = {
            "price": ['float']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="greater_than">
<h2 class="text-xl font-bold mt-6">greater_than</h2>
<rule>greater_than:another_field</rule>

<p class="text-wrap my-3">
    The greater_than rule is used to check if a field is greater than another field. If the field is not greater than the specified field, the greater_than rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The greater_than rule takes one argument, another_field, which is the referenced field.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "age_limit": 20,
            "age": 24,
        }

        rule = {
            "age": ['greater_than:age_limit'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="greater_than_or_equal">
<h2 class="text-xl font-bold mt-6">greater_than_or_equal</h2>
<rule>greater_than_or_equal:another_field</rule>

<p class="text-wrap my-3">
    The greater_than_or_equal rule is used to check if a field is greater than or equal to another field. If the field is not greater than or equal to the specified field, the greater_than_or_equal rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The greater_than_or_equal rule takes one argument, another_field, which is the referenced field.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "age_limit": 20,
            "age": 20,
        }

        rule = {
            "age": ['greater_than:age_limit'],
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="in">
<h2 class="text-xl font-bold mt-6">in</h2>
<rule>in:foo,bar...</rule>

<p class="text-wrap my-3">
    The in rule is used to check if a field is in a list of comma separated values. If the field is not in the list of values, the in rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The in rule takes one argument, "foo, bar", which is a comma-separated list of values that the field should be in.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "age": 20
        }

        rule = {
            "age": ['in:20,21,23,25']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="integer">
<h2 class="text-xl font-bold mt-6">integer</h2>
<rule>integer</rule>

<p class="text-wrap my-3">
    The integer rule checks if a field contains a valid integer
</p>
<p class="text-wrap my-3">
    The integer rule takes no argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "age": 20
        }

        rule = {
            "age": ['integer']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="less_than">
<h2 class="text-xl font-bold mt-6">less_than</h2>
<rule>less_than:another_field</rule>

<p class="text-wrap my-3">
    The less_than rule checks if the field under validation is less than the value in another field
</p>
<p class="text-wrap my-3">
    The less_than rule takes one argument, another_field, which is the referenced field.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "wallet_balance": 20000,
            "price": 5000
        }

        rule = {
            "price": ['less_than:wallet_balance']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="less_than_or_equal">
<h2 class="text-xl font-bold mt-6">less_than_or_equal</h2>
<rule>less_than_or_equal:another_field</rule>

<p class="text-wrap my-3">
    The less_than_or_equal rule checks if the field under validation is less than or equals a value in another field
</p>
<p class="text-wrap my-3">
    The less_than_or_equal rule takes one argument, another_field, which is the referenced field.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "wallet_balance": 20000,
            "price": 5000
        }

        rule = {
            "price": ['less_than_or_equal:wallet_balance']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="list">
<h2 class="text-xl font-bold mt-6">list</h2>
<rule>list</rule>

<p class="text-wrap my-3">
    The list rule verifies if a value is a valid list
</p>
<p class="text-wrap my-3">
    The list rule takes no argument.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "students": ['Joy', 'Joel', 'Kenn', 'Kay']
        }

        rule = {
            "students": ['list']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="lowercase">
<h2 class="text-xl font-bold mt-6">lowercase</h2>
<rule>lowercase</rule>

<p class="text-wrap my-3">
    The lowercase rule checks if all the characters in a value are all lowercases.
</p>
<p class="text-wrap my-3">
    The lowercase rule does not take any argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "model": "tedds"
        }

        rule = {
            "model": ['lowercase']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="max">
<h2 class="text-xl font-bold mt-6">max</h2>
<rule>max:maximum_value</rule>

<p class="text-wrap my-3">
    The max rule is used to check if a field's value is less than or equal to a specified minimum value. If the field's value is less than the specified minimum value, the min rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The max rule takes one argument, maximum_value, which is the maximum value that the field should have.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "password": "1234Point"
        }

        rule = {
            "password": ['max:12']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="mimes">
<h2 class="text-xl font-bold mt-6">mimes</h2>
<rule>mimes:foo,bar....</rule>

<p class="text-wrap my-3">
    The mimes rule is used to check if a file has a specified MIME type. If the file does not have the specified MIME type, the mimes rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The mimes rule takes comma seperated arguments, which are the MIME types that the file should have.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "photo": "selfie.jpg"
        }

        rule = {
            "photo": ['mimes:jpg,png']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="min">
<h2 class="text-xl font-bold mt-6">min</h2>
<rule>min:minimum_value</rule>

<p class="text-wrap my-3">
    The min rule is used to check if a field's value is greater than or equal to a specified minimum value. If the field's value is less than the specified minimum value, the min rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The min rule takes one argument, minimum_value, which is the minimum value that the field should have.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "password": "1234Point"
        }

        rule = {
            "password": ['min:6']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="not_in">
<h2 class="text-xl font-bold mt-6">not_in</h2>
<rule>not_in:foo,bar...</rule>

<p class="text-wrap my-3">
    The not_in rule is used to check if a field is not in a list of comma-separated values. If the field is in the list of values, the not_in rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The not_in rule takes one argument, "foo, bar", which is a comma-separated list of values that the field should not be in.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "weekday": "monday"
        }

        rule = {
            "weekday": ['not_in:sunday,saturday']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="required">
<h2 class="text-xl font-bold mt-6">required</h2>
<rule>required</rule>

<p class="text-wrap my-3">
    The required rule is used to check if a field is present in the data. If the field is not present, the required rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The required rule does not take any arguments.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "John Doe",
            "email": "john@ratify.com",
            "age": 25
        }

        rule = {
            "name": ['required'],
            "email": ['required'],
            "age": ['required']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="required_if">
<h2 class="text-xl font-bold mt-6">required_if</h2>
<rule>required_if:another_field,foo..</rule>

<p class="text-wrap my-3">
    The required_if rule makes a field required when a specified field contains a specified value
</p>
<p class="text-wrap my-3">
    The required_if rule takes a comma seperated argument which starts with the referenced field as the first value, then the specified values
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "John Doe",
            "country": "Canada",
            "zip_code": "100 WYM",
            "email": "john@ratify.com",
            "age": 25
        }

        rule = {
            "zip_code": ['required_if:country,Canada,USA']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="same">
<h2 class="text-xl font-bold mt-6">same</h2>
<rule>same:another_field</rule>

<p class="text-wrap my-3">
    The same rule is used to check if a field matches another field. If the field does not match the other field, the same rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The same rule takes one argument, another_field, which is the field that the field should match.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "email": "john@ratify.com",
            "confirm_email": "john@ratify.com"
        }

        rule = {
            "confirm_email: ['same:email']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="size">
<h2 class="text-xl font-bold mt-6">size</h2>
<rule>size:value</rule>

<p class="text-wrap my-3">
    The size rule is used to check if a field's value is equal to a specified size. If the field's value is not equal to the specified size, the size rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    This validates integers, strings and lists. when used on integers, the field under validation must be equal to the specified value, for strings it validates the string's length, for lists it validates the list length.
</p>
<p class="text-wrap my-3">
    The size rule takes one argument, value, which is the specified value
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "age": 20,
            "key": "Everyday",
            "names": ["Rahman", "Kola", "Chike"]
        }

        rule = {
            "age": ['size:20'],
            "key": ['size:8'],
            "names": ['size:3']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="starts_with">
<h2 class="text-xl font-bold mt-6">starts_with</h2>
<rule>starts_with:value</rule>

<p class="text-wrap my-3">
    The starts_with rule checks if a field starts with a specified value. If the field does not start with the specified value, the starts_with rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The starts_with rule takes one argument, value, which is the value that the field should start with.
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "Everyday"
        }

        rule = {
            "name": ['starts_with:Ev']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="string">
<h2 class="text-xl font-bold mt-6">string</h2>
<rule>string</rule>

<p class="text-wrap my-3">
    The string rule checks if a field is a valid string. If the field is not a valid string, the string rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The string rule takes no argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "name": "Everyday19"
        }

        rule = {
            "name": ['string']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)
</div>

</div>

<div class="px-4 py-12 min-h-[100vh]" id="uppercase">
<h2 class="text-xl font-bold mt-6">uppercase</h2>
<rule>uppercase</rule>

<p class="text-wrap my-3">
    The uppercase rule checks if all the characters in a value are all uppercases.
</p>
<p class="text-wrap my-3">
    The uppercase rule does not take any argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "model": "TEDDS"
        }

        rule = {
            "model": ['uppercase']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                         
</div>

</div>


<div class="px-4 py-12 min-h-[100vh]" id="url">
<h2 class="text-xl font-bold mt-6">url</h2>
<rule>url</rule>

<p class="text-wrap my-3">
    The url rule checks if a field is a valid URL. If the field is not a valid URL, the url rule raises a ValidationError exception.
</p>
<p class="text-wrap my-3">
    The url rule does not take any argument
</p>

<div class="bg-gray-100 p-4 rounded-lg text-center flex cursor-pointer justify-between mt-3 w-full">
    from ratify.ratify import Ratify

    validator = Ratify()

    try:
        data = {
            "website": "https://ted.com"
        }

        rule = {
            "webiste": ['url']
        }

        validated = validator.make(data, rule)
    except ValidationError as e:
        print(e)                         
</div>

</div>
