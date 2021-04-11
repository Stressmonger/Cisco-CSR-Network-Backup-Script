import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Please enter username: ")
PASSWORD = getpass("Please enter password: ")

device = {
      'ip': '192.168.204.11',
	  'username': USERNAME,
	  'password': PASSWORD,
	  'device_type': 'cisco_ios'
	  }
	  
      
connect = ConnectHandler(**device)
	  
output = connect.send_command('show run')

bak = open('backup.conf', 'x')

bak.write(output)
bak.close

