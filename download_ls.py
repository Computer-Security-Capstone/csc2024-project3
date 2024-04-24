#!/usr/bin/python3
import paramiko
import sys
import os

username = "csc2024"
password_filename = "password"

null = open(os.devnull, "w")
sys.stderr = null

with open(password_filename, "r") as file:
    password = file.read()
    while True:
        try:
            transport = paramiko.Transport((sys.argv[1], 22))
            transport.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get("/bin/ls", os.path.abspath(os.getcwd()) + "/orgi_ls")
            break
        except KeyboardInterrupt:
            exit()
        except:
            pass

    transport.close()