import socket
import sys
import random
import functions
import pickle
import numpy as np

listenClient = 0
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())

port = 5131

serversocket.bind((host, port))
serversocket.listen(1)

print("Use this port to connet to server : ", port)

print("Started the server :)")

serversocket, addr = serversocket.accept()
print("Got a connection from", addr)
print('Ready to play') 
rematch = 'N'
Boardis = []

print(functions.modifyTable(functions.board))

end = True
while end:
    askToplay = input('what do you want to choose X or O : ')
    theBoard = np.array(functions.board)
    if askToplay == "bb":
     print("Thankyou Terminating server connection..")
     sys.exit(0)

    # establish a connection
    while askToplay == 'O':
        print('Client is still playing ... ..... ........')
        try:
            encoded_arr = serversocket.recv(1024)
            boardFromClient = pickle.loads(encoded_arr)
            if str(boardFromClient) == 'end':
                end = False
                print('Client ended the game')
                break
        except EOFError:
            print('client won the game')
            rematch = input('Do you wanna try again?? if so type Y or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = theBoard
                break
        
            
        if(str(boardFromClient) == 'won' or functions.checkWin(boardFromClient,'X') == True):
            print('Client -> \n', functions.modifyTable(boardFromClient))
            print('Client Won the Match... :-_- -_- -_- -_-')
            rematch = input('Do you wanna try again?? if so type Y or N : ')
            if rematch == 'N' or rematch =='n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = theBoard
                break
        print('client -> \n',functions.modifyTable(boardFromClient))
        print('Enter row and column number to position your O')
        try:
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
        except ValueError:
            print('Enter interger value')
        if functions.checkEmptyElement(boardFromClient,row,clm) == True:
            boardFromClient[row-1,clm-1] = 'O'
        if functions.checkEmptyElement(boardFromClient,row,clm) == False:
            print('Element exists!!! Choose another row and column')
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
            boardFromClient[row-1,clm-1] = 'O'
        print(functions.modifyTable(boardFromClient))
        if functions.checkTie(boardFromClient,'O'):
            print('Match Tied..')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = np.array(functions.board)
                codeArray = pickle.dumps(boardFromClient)
                serversocket.sendall(codeArray)
                break
        if functions.checkWin(boardFromClient,'O') == True:
            print('You won the game..... :) :) :) :)')
            codeArray = pickle.dumps(boardFromClient)
            serversocket.sendall(codeArray)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = np.array(functions.board)
                codeArray = pickle.dumps(boardFromClient)
                serversocket.sendall(codeArray)
                break
        codeArray = pickle.dumps(boardFromClient)
        serversocket.sendall(codeArray)
        if functions.checkTie(boardFromClient,'O'):
            print('Match Tied..')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = np.array(functions.board)
                codeArray = pickle.dumps(boardFromClient)
                serversocket.sendall(codeArray)
                break
    
    while askToplay == 'X':
        print('Enter row and column number to position your X')
        try:
            row = int(input('Enter row fg: '))
            clm = int(input('Enter column: '))
        except ValueError:
            print('Enter interger value')
        if functions.checkEmptyElement(theBoard,row,clm) == True:
            theBoard[row-1,clm-1] = 'X'
        else:
            print('Element exists!!! Choose another row and column')
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
            theBoard[row-1,clm-1] = 'X'
        print(functions.modifyTable(theBoard))
        if functions.checkTie(theBoard,'X'):
            print('Match Tied..')
            codeArray = pickle.dumps(theBoard)
            serversocket.sendall(codeArray)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        print('Waiting for client.. .... ........')
        if functions.checkWin(theBoard,'X') == True:
            print('You won the game..... :) :) :) :)')
            codeArray = pickle.dumps(theBoard)
            serversocket.sendall(codeArray)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                codeArray = pickle.dumps('end')
                serversocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        codeArray = pickle.dumps(theBoard)
        serversocket.sendall(codeArray)
        ## Receive from client
        encoded_arr = serversocket.recv(1024)
        boardFromClient = pickle.loads(encoded_arr)
        if str(boardFromClient) == 'end':
            end = False
            break
        if str(boardFromClient) == 'won':
            print('Client won the game -_- -_- -_- -_- ')
            break
        theBoard = boardFromClient
        print('client -> \n',functions.modifyTable(theBoard))
        if functions.checkWin(theBoard,'O'):
            print('Client won the game..... -_- -_- -_- -_-')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                codeArray = pickle.dumps('end')
                serversocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        if functions.checkTie(theBoard,'O'):
            print('Match Tied..')
            codeArray = pickle.dumps(theBoard)
            serversocket.sendall(codeArray)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
    
       
print("Its a nice Game")

    
