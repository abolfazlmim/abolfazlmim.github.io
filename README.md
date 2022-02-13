# abolfazlmim.github.io
My personal webpage on github pages 





import platform
import subprocess
def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '5', host]
    response = subprocess.call(command)
    if response == 0:
        return True
    else:
        return False
print(myping("www.google.com"))

-------------
import os
def myping(host):
    response = os.system("ping -c 3 " + host)
    if response == 0:
        return True
    else:
        return False
print(myping("www.google.com"))


.

