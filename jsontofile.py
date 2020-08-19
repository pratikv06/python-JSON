import json

json_equivalent_dict = {"json": "python", 
"object": "dict", 
"array": ["list", "tuple"], 
"string": "str", 
"number": ["int", "float"], 
"true": "True", 
"false": "False", 
"null": "None"
}

with open('json_equivalent.txt', 'w') as f:
    json.dump(json_equivalent_dict, f, indent = 4, sort_keys=True)