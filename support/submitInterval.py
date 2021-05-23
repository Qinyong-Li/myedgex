import requests
import json

url='http://localhost:48085/api/v1/interval'

# read requestbody from json_file
file=open('./interval/emailinterval.json')
data_json=json.dumps(json.load(file))

# submit interval by "POST"
r=requests.post(url=url,data=data_json)

# print result
print(r.status_code)
print(r.text)

# clean up
file.close()