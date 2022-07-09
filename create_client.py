import requests
import json

def client_creation():
    url = "url of the service to be called"
    with open("body_clientCreation.json", "r") as read_file:
         data1 = json.load(read_file)
    # print("######################################################") 
    # print(json.dumps(data1))    
    headers = {
    'Authorization': 'Basic token',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data1), verify = False)
    print(response.text)
    files = response.json()
    return files["client_id"], files["client_secret"]

    # print(response.json)
