import socket
import sys
def connectServer(ip, port):
    global remoteIP, session
    session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
       session.connect((ip, port))
       print("[+]Connection is build up")
       banner()

    except:
        print("[-]Can not connect")
    remoteIP = ip
    prompt()

def prompt():
    while True:
          command = input("[%s]$" % remoteIP)
          if command == "exit":
              session.close()
          try:
              session.send(command.encode())
          except:
              print("[-]Can not send the command")

          data = session.recv(1024)
          print((data.decode()))
def banner():
    print("""                 ######  ####### ######        #     #    #    ####### ####### ####### ######
                     #     # #       #     #       ##   ##   # #      #       #    #       #     #
                     #     # #       #     #       # # # #  #   #     #       #    #       #     #
                     ######  #####   #     #       #  #  # #     #    #       #    #####   ######
                     #   #   #       #     #       #     # #######    #       #    #       #   #
                     #    #  #       #     #       #     # #     #    #       #    #       #    #
                     #     # # # # #  # # #        #     # #     #    #       #    # # # # #      # """)

if len(sys.argv) != 3:
    print("python console.py ip port")
    sys.exit()

else:
    connectServer(sys.argv[1], int(sys.argv[2]))


