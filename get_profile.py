import requests


def get_profile():
    url = "url of the service to be called"
    payload={}    
    headers = {
      'Authorization': 'Bearer token'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

