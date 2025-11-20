import os
import json

current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")


data = {"name": "Prime", "age": 23}

json_string = json.dumps(data)

print(f"Json string: {json_string}")