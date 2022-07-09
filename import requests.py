import requests
import json

url = "url of the server"

payload = json.dumps({
  "iccid": "iccid",
  "mnoId": "customer-id",
  "allowedRequesterId": "customer-id",
  "profileType": "GSMA Profile Package",
  "state": "AVAILABLE",
  "subscriptionAddress": {
    "imsi": "imsi",
    "msisdn": "msisdn"
  },
  "profileMetaData": {
    "operatorServiceProviderName": "customer-id",
    "profileName": "customer-id Profile 1",
    "iconType": 1,
    "icon": "icon of profile in hex",
    "profileClass": "OPERATIONAL",
    "profileOwner": {
      "mccMnc": "mcc mnc value of operator"
    },
    "notificationConfigurationInfo": [
      {
        "notificationAddress": "customer fqdn",
        "notificationDisable": True,
        "notificationInstall": True,
        "notificationEnable": True,
        "notificationDelete": True
      }
    ],
    "profilePolicyRules": [
      False,
      False
    ]
  },
  "upp": "binary data",
  "verificationCertificateVersion": "1",
  "decryptionKeyVersion": 1
})
headers = {
  'Authorization': 'Bearer token',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
