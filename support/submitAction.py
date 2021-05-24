import requests
import json

url = 'http://localhost:48085/api/v1/intervalaction'

# read notification detail from json_file
notification_file = open('./notification/email.json')
notification_json = json.load(notification_file)

# read action requestbody from json_file
action_file=open("./intervalAction/emailAction.json")
action_json=json.load(action_file)

# intert parameter to action requestbody
# action_json["parameters"]=notification_json
data_json=json.dumps(action_json)
# print(type(notification_json["labels"]))
print(data_json)

# submit interval action with POST
r=requests.put(url=url,data=data_json)
print(r.status_code)
print(r.text)

# clean up
notification_file.close()
action_file.close()
