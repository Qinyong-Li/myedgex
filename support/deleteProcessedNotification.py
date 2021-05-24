import requests
import json

def deleteNotification(result,delete_url):
    # delete notification with processed status
    for i in range(len(result)):
        status=result[i]["status"]
        if status == "PROCESSED":
            slug=result[i]["slug"]
            url=delete_url+slug
            r=requests.delete(url=url)
            print(r.status_code)

query_url='http://localhost:48060/api/v1/notification/sender/qinyong@163.com/0'
delete_url='http://localhost:48060/api/v1/notification/slug/'

# query notification which status is processed
r=requests.get(query_url)
result_json=r.text
if r.status_code==200:
    result=json.loads(result_json)
    deleteNotification(result=result,delete_url=delete_url)
else:
    print(r.status_code)
    print(r.text)