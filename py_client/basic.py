import requests
# import json

endpoint = "http://localhost:8000/api/"
# endpoint = 'http://httpbin.org/anything'
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
get_response  = requests.get(endpoint, json=data)
# print(get_response.json)
print(get_response.json())

