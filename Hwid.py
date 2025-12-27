from time import sleep
import requests
import subprocess
from os import system
import sys
from hashlib import sha256
import hashlib

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        sleep(0.1)

r = requests.get("https://pastebin.com/raw/zXNKxtaa")
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())

system("cls & title " + "HWID-LOCK │ By NewYear`z#5505")
def checking():
	sleep(0.5)  
	if hashlib.sha256(hwid.encode('utf-8')).hexdigest() in r.text:
		return True
	return False
sleep(0.5)

if (checking() != True):
    printSlow("HWID >>>> ")
    print(sha256("{hwid}".encode()).hexdigest())
    input()
    exit()
print('LOGIN SUCCESS')
sleep(0.5)