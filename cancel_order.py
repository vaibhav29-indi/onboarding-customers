import requests
import json


def cancel_order():
    url = "<url of the service to be called"
    payload = json.dumps({
    "header": {
    "functionRequesterIdentifier": "customer-name",
    "functionCallsIdentifier": "TX-567"
    },
    "iccid": "iccid",
    "eid": "eid",
    "matchingId": "token",
    "finalProfileStatusIndicator": "Available"
    })
    headers = {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
