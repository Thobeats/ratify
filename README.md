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
        <code class="language-bash text-left text-sm">
            from ratify.ratify import Ratify <br> <br>

            validator = Ratify() <br><br>
            try: <br>
                &nbsp;&nbsp; data = { <br>
                &nbsp;&nbsp;&nbsp;&nbsp; "name": "John Doe", <br>
                &nbsp;&nbsp;&nbsp;&nbsp; "email": "john@ratify.com", <br>
                &nbsp;&nbsp;&nbsp;&nbsp; "age": 25 <br>
                &nbsp;&nbsp; } <br><br>

                &nbsp;&nbsp; rule = { <br>
                &nbsp;&nbsp;&nbsp;&nbsp;"name": ['required'],<br>
                &nbsp;&nbsp;&nbsp;&nbsp;"email": ['required', 'email'],<br>
                &nbsp;&nbsp;&nbsp;&nbsp;"age": ['required', 'integer', 'max:30']<br>
                &nbsp;&nbsp;} <br>

                &nbsp;&nbsp;validated = validator.make(data, rule) <br>
            except ValidationError as e: <br>
                &nbsp;&nbsp;print(e) <br>                         
        </code>
        <span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75" />
            </svg>
        </span>                      
    </div>

</div>