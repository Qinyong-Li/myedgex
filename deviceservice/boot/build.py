import subprocess

child1=subprocess.Popen("cd ../build && cmake .. && make && cp main ../", shell=True)
child1.wait()
