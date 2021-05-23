import requests
import json

header={
    'accept': '*/*',
    'Content-Type': 'application/json'
}
url='http://localhost:48060/api/v1/notification'

# read notification requestBody from json_file
file=open("./notification/email.json")
data_json=json.dumps(json.load(file))

# register notification
r=requests.post(url=url,data=data_json,headers=header)

# print result of registration
print(r.status_code)
print(r.text)

# clean up
file.close()
