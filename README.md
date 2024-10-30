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
