from os import times
import subprocess
import requests
import json
import yaml
import time
import signal

def stop(signal,frame):
    print("stop")

subprocess.call("python3 build.py",shell=True)
p=subprocess.Popen("../main",shell=True)
time.sleep(1)
p.kill()
child=subprocess.Popen("../main",shell=True)
signal.signal(signal.SIGINT,stop)
signal.pause()
child.kill()
subprocess.call("python3 clean.py",shell=True)