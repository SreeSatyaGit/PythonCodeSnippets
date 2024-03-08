import socket
import sys

listenServer = 0
# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = input("Enter server portnumber to connect :")

# connection to hostname on the port.
clientsocket.connect((host, int(port)))

greetMesgs = ['hi','hello','good morning','how are you']

def checkMesgInGreet (mesg):
    for checkGreet in greetMesgs:
        if mesg == checkGreet:
            return True
        else:
            return False

while True:
    while listenServer == 0:
        MessgToClient = input(" Send message to server : ")
        clientsocket.send(MessgToClient.encode())
        if MessgToClient == "x":
            print("Asking server to chat")
            listenServer = 1
            break
        if MessgToClient == "xx":
            print("Thank you, Terminating client connection")
            sys.exit(0)
        mesgFromServer = clientsocket.recv(1024).decode()
        print("Sever:Message Received ->",mesgFromServer)

    while listenServer == 1:
         msg = clientsocket.recv(1024).decode()
         print("Message From Server:",msg)
         if msg == "x":
            print(" Sever is asking to chat..")
            listenServer = 0
            break
         if msg == "xx":
            print("Thank you, Terminating client connection")
            sys.exit(0)
