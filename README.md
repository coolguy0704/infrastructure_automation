# infrastructure_automation
Infrastructure automation using python paramiko modules. Login to each server/VM/Container in the infrastructure and execute commands. (Assuming there's a use case where using ansible is not allowed and only default python modules such as os, sys, paramiko etc. are allowed.)


Execution example:

$ python paramiko <username> <key_file_location>

username: will the username to be used to login to server
key_file_location: key file used to login to server
