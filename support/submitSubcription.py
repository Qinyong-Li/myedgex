import requests
import json

url='http://localhost:48060/api/v1/subscription'

# read requestbody
f=open("./subscription/email.json")
data_json=json.dumps(json.load(f))

# register
r=requests.post(url=url,data=data_json)

#print result
print(r.status_code)
print(r.text)

# clean up
f.close()