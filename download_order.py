import requests
import json


def download_order():
    url = "url of the service to be called"
    payload = json.loads(./body_uploadprofile.json)
    headers = {
    'Authorization': 'Basic token',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)



payload = json.dumps({
  "header": {
    "functionRequesterIdentifier": "customer-id",
    "functionCallerIdentifier": "customer-id"
  },
  "iccid": "iccid"
})
headers = {
  'Content-Type': 'application/json',
  'X-Admin-Protocol': 'gsma/rsp/v2.0.0',
  'Authorization': 'Bearer token'
}


