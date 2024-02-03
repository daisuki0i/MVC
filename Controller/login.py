import json
import os

# read the json file from the ../Model/database.json
def read_json():
    print(os.getcwd())
    with open('Model/database.json') as f:
        data = json.load(f)
    return data

def check_credential(username, password):
    data = read_json()
    for user in data:
        if user['username'] == username and user['password'] == password:
            return True
    return False
    