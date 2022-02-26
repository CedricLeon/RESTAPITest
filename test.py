########################################
# Test file to send request to the API #
########################################

import requests

BASE = "http://127.0.0.1:5000/"

# Some data to put in the DB the first time
data = [{"name": "cedric", "gender": "male", "age": 23},
        {"name": "lucie", "gender": "female", "age": 22},
        {"name": "ivan", "gender": "male", "age": 20}]

#for i in range(len(data)):
#    response = requests.put(BASE + "client/" + str(i), data[i])
#    print(response.json())

# --- Check the delete method (/!\ output is not json) ---
#response = requests.delete(BASE + "client/0")
#print(response)

# --- GET method test ---
response = requests.get(BASE + "client/0")
print(response.json())

x = input()

# --- PUT method test ---
response = requests.put(BASE + "client/0", {"name": "cedric", "gender": "male", "age": 17})
print(response.json())

x = input()

# --- PATCH method ---
response = requests.patch(BASE + "client/1", {"age": 53})
print(response.json())
