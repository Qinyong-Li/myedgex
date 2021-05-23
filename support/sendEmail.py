import subprocess
import time

# register notification and subcription
subprocess.call("python3 submitSubcription.py",shell=True)
subprocess.call("python3 submitNotification.py",shell=True)
time.sleep(1)

# clean up
subprocess.call("python3 deleteProcessedNotification.py",shell=True)