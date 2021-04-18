import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USERNAME = input("Please enter username: ")
PASSWORD = getpass("Please enter password: ")

device = {
      'ip': '192.168.204.11',
	  'username': USERNAME,
	  'password': PASSWORD,
	  'device_type': 'cisco_ios'
	  }
	  
     
try:     
    connect = ConnectHandler(**device)
	  
    output = connect.send_command('show run')

    bak = open('backup.conf', 'x')   

    bak.write(output)
    bak.close()

except (AuthenticationException):
         print("Authentication error when connecting to:" + device['ip'])
         
except (NetMikoTimeoutException):
         print("The connection to " + device['ip'] + " has timed out")
         
except (SSHException):
         print("SSH protocol error has occured when connecting to " + device['ip'])
         

         
         
