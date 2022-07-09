import requests
import json

def confirm_order():
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
    "functionRequesterIdentifier": "id of the mvno",
    "functionCallIdentifier": "id of the mvno"
  },
  "iccid": "iccid",
  "matchingId": "token",
  "releaseFlag": True
})
headers = {
  'Content-Type': 'application/json',
  'X-Admin-Protocol': 'gsma/rsp/v2.0.0',
  'Authorization': 'Bearer token'
}


