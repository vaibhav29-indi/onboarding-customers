import base64

data = "customer" + ":" + "xyz"
data1 = base64.b64encode(data.encode())
auth_header = "Basic" +" " + str(data1,'utf-8') 
print(auth_header)
# client_account = "'" + clientId + "'"
# print(auth_header)
