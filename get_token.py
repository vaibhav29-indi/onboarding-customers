import requests
import base64

def client_token(clientId,secret):
    data = clientId + ":" + secret
    data1 = base64.b64encode(data.encode())
    auth_header = "Basic" +" " + str(data1,'utf-8')
     
    # print(auth_header)  
    url = "url of the server"
    print(auth_header)
    payload={'grant_type': 'client_credentials',
      'client_id': clientId
    }
    print(payload)
    files=[
    ]
    headers = {
    'Authorization': auth_header
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files, verify = False)
    print(response.text)
    files = response.json()
    return files["access_token"]



