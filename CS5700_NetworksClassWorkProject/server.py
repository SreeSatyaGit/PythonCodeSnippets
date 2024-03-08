import socket
import sys
import random

listenClient = 0
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = random.randint(1024,65535)

serversocket.bind((host,port))
serversocket.listen(5)

print("Use this port to connet to server : ", port)

print("The server is ready to receive")

clientsocket, addr = serversocket.accept()
print("Got a connection from", addr)

greetMesgs = ['hi','hello','good morning']

def checkMesgInGreet (mesg):
    for checkGreet in greetMesgs:
        if mesg == checkGreet:
            return True
        else:
            return False



while True:
    # establish a connection
    while listenClient == 0:
        msg = clientsocket.recv(1024).decode() 
        if not msg:
            break
        print("Client:", msg)
        if checkMesgInGreet(msg):
            clientsocket.send("Hey Buddy, how are you...".encode())
        else:
            if msg != "x":
                clientsocket.send(msg.encode())
        if msg == "x":
            listenClient = 1
            print("Client is asking to chat..")
            break
        if msg == "xx":
            print("Thankyou Terminating server connection..")
            sys.exit(0)
       
    while listenClient == 1:
        MesgToClient = input("Message to client : ")
        if MesgToClient == "x":
            listenClient = 0
            break
        clientsocket.send(MesgToClient.encode())
        if MesgToClient == "xx":
            print("Thank you Terminating the  server connection!")
            sys.exit(0)

