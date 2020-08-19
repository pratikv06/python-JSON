'''
json.dumps() method can convert a Python object into a JSON string.
json.dump() method can be used for writing to JSON file.
'''

import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)


json_equivalent_dict = {'json': 'python',
'object': 'dict',
'array': ['list', 'tuple'],
'string': 'str',
'number': ['int', 'float'],
'true': 'True',
'false': 'False',
'null': 'None'
}

json_equivalent = json.dumps(json_equivalent_dict)
print(json_equivalent)
print(type(json_equivalent))