import requests

def delete_order():
    url = "url of the service to be called"
    payload = ""
    headers = {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)





