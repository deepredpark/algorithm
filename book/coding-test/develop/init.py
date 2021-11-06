# import json

# user = {
#   "id": "gildong",
#   "password": "1!2@3#4$",
#   "age": 30,
#   "hobby": ["football", "programming"]
# }

# with open("user.json", "w", encoding="utf-8") as file:
#   json_data = json.dump(user, file, indent=4)

import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()

name_list = []
for user in data:
  name_list.append(user['name'])

print(name_list)
