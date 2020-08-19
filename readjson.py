'''
Yes, `s` stands for string. The json.loads function does not take the file path, 
but the file contents as a string. 
Look at the documentation at https://docs.python.org/2/library/json.html!
'''

import json

with open('person.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)