import requests
import json

interval_url = 'http://localhost:48085/api/v1/interval'
action_url = 'http://localhost:48085/api/v1/intervalaction'

# get intervalaction name and interval name
r1 = requests.get(action_url)
r2 = requests.get(interval_url)
interval_json = json.loads(r2.text)
action_json = json.loads(r1.text)

# delete interval and intervalaction
for i in range(len(action_json)):
    name = action_json[i]["name"]
    delete_url = action_url+'/name/'+name
    print(delete_url)
    r_temp = requests.delete(url=delete_url)
    if r_temp.status_code != 200:
        print(r_temp.status_code)
        print(r_temp.text)


for i in range(len(interval_json)):
    name = interval_json[i]["name"]
    delete_url = interval_url+'/name/'+name
    r_temp = requests.delete(url=delete_url)
    print(delete_url)
    if r_temp.status_code != 200:
        print(r_temp.status_code)
        print(r_temp.text)
