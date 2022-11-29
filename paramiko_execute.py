# -*- coding: utf-8 -*-

from __future__ import print_function
from StringIO import StringIO
import paramiko
import time
import sys
import re
import os

print()
username = sys.argv[1]
file = open(sys.argv[2],'r')
s = file.read()
key_file = StringIO(s)
pkey = paramiko.RSAKey.from_private_key(key_file)
#commands = ['ls', 'pwd', 'hostname', 'who']
with open('hosts_list.txt') as ip_file:
    lines = ip_file.read().splitlines()
    for line in lines:
        print("-------------------------------------------------------------------")
        print("running commands in IP address: ",line)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=line, username=username, pkey=pkey)
        print("-------------------------------------------------------------------")
        with open('commands.txt') as cmd_file:
            cmd_lines = cmd_file.read().splitlines()
            for cmd_line in cmd_lines:
                stdin,stdout,stderr = ssh_client.exec_command(cmd_line, get_pty=True)
                print("executed command: ", cmd_line)
                for line in iter(stdout.readline, ""):
                    print(line, end ="")
                exit_status = stdout.channel.recv_exit_status()
                if exit_status == 0:
                    #print("command executed")
                    continue
                else:
                    print("Error", exit_status)
                #print(stdout.read())
                err = stderr.read().decode()
                if err:
                    print(err)
        print(); print(); print()
        ssh_client.close()