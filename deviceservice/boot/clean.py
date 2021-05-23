import requests
import subprocess

cmd1 = "curl -X 'DELETE' http://localhost:48081/api/v1/deviceservice/name/device-template"
cmd2 = "curl -X 'DELETE' http://localhost:48081/api/v1/deviceprofile/name/RandNum-Device"

subprocess.call(cmd1,shell=True)
subprocess.call(cmd2,shell=True)