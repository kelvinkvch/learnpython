import requests

# get data from an api
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
