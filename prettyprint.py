import json

json_equivalent = '{"json": "python", "object": "dict", "array": ["list", "tuple"], "string": "str", "number": ["int", "float"], "true": "True", "false": "False", "null": "None"}'

# Getting dictionary
json_dict = json.loads(json_equivalent)

# Pretty Printing JSON string back
print(json.dumps(json_dict, indent = 4, sort_keys=True))