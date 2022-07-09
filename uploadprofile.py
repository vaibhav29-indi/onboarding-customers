import requests
import json
import main


def profile_upload():
    url = "url of the server"
    payload = json.loads(./body_uploadprofile.json)
    headers = {
    'Authorization': 'Basic token',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


