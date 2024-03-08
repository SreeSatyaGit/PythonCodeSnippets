import socket
import sys
import functions
import pickle
import numpy as np
listenServer = 0
# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = input("Enter server portnumber to connect :")


# connection to hostname on the port.
clientsocket.connect((host, int(port)))

rematch = 'N'

print('Ready to play') 
print(functions.modifyTable(functions.board))
end = True
while end:
    askToplay = input('what do you want to choose X or O : ')
    theBoard = np.array(functions.board)
    while askToplay == 'O':
        print('Server is still playing ... ..... ........')
        encoded_arr = clientsocket.recv(1024)
        try:
            boardFromServer = pickle.loads(encoded_arr)
            if str(boardFromServer) == 'end':
                print('Server ended the match')
                end = False
                break
        except EOFError:
            print('Server Won the Match... :( :( :( :(')
            rematch = input('Do you wanna try again?? if so type Y or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
            if rematch == 'Y' or rematch == 'y':
                encoded_arr = clientsocket.recv(1024)
                boardFromServer = pickle.loads(encoded_arr)
        if(functions.checkWin(boardFromServer,'X') == True):
            print('Server -> \n',functions.modifyTable(boardFromServer))
            print('Server Won the Match... :( :( :( :(')
            rematch = input('Do you wanna try again?? if so type Y or N : ')
            if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        else:
            print('Server -> \n',functions.modifyTable(boardFromServer))
            print('Enter row and column number to position your O')
        if functions.checkTie(boardFromServer,'X'):
             print('Server -> \n',functions.modifyTable(boardFromServer))
             print('Match Tied')
             rematch = input('Do you wanna try again?? if so type Y or N : ')
             if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
             if rematch == 'Y' or rematch == 'y':
                break
        try:
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
        except ValueError:
            print('Enter interger value')
        if functions.checkEmptyElement(boardFromServer,row,clm) == True:
           boardFromServer[row-1][clm-1] = 'O'
        else:
            print('Element exists!!! Choose another row and column')
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
            boardFromServer[row-1][clm-1] = 'O'   
        
        if str(boardFromServer) == 'end':
            end = False
            break
        print(functions.modifyTable(boardFromServer))
        if functions.checkWin(boardFromServer,'O') == True:
            codeArray = pickle.dumps(boardFromServer)
            clientsocket.sendall(codeArray)
            print('You won the game..... :) :) :) :)')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        print('Waiting for server .. .... ........')
        codeArray = pickle.dumps(boardFromServer)
        clientsocket.sendall(codeArray)

    while askToplay == 'X':
        print('Enter row and column number to position your X')
        try:
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
        except ValueError:
            print('Enter interger value')
        
        if functions.checkEmptyElement(theBoard,row,clm) == True:
           theBoard[row-1][clm-1] = 'X'
        else:
            print('Element exists!!! Choose another row and column')
            row = int(input('Enter row: '))
            clm = int(input('Enter column: '))
            theBoard[row-1][clm-1] = 'X'
        if functions.checkTie(theBoard,'O'):
            print('Match Tied..')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                boardFromClient = np.array(functions.board)
                codeArray = pickle.dumps(boardFromClient)
                clientsocket.sendall(codeArray)
                break
        print(functions.modifyTable(theBoard))
        if functions.checkWin(theBoard,'X') == True:
            codeArray = pickle.dumps(theBoard)
            clientsocket.sendall(codeArray)
            print('You won the game..... :) :) :) :)')
            theBoard = np.array(functions.board)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        if functions.checkTie(theBoard,'O'):
             print('Server -> \n',functions.modifyTable(theBoard))
             print('Match Tied')
             rematch = input('Do you wanna try again?? if so type Y or N : ')
             if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
             if rematch == 'Y' or rematch == 'y':
                break
        codeArray = pickle.dumps(theBoard)
        clientsocket.sendall(codeArray)
        ## Receive from server
        encoded_arr = clientsocket.recv(1024)
        theBoard = pickle.loads(encoded_arr)
        print('Server -> \n',functions.modifyTable(theBoard))
        if str(theBoard) == 'end':
            end = False
            break
        if functions.checkWin(theBoard,'O') == True:
            print('Server won the game..... :( :( :( :(')
            codeArray = pickle.dumps(theBoard)
            clientsocket.sendall(codeArray)

            codeArray = pickle.dumps('won')
            clientsocket.sendall(codeArray)
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n' :
                codeArray = pickle.dumps('end')
                clientsocket.sendall(codeArray)
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        if functions.checkTie(theBoard,'O'):
            print('Match Tied..')
            rematch = input('Do you wanna Re-Match?. Type Y if so or N : ')
            if rematch == 'N' or rematch == 'n':
                end = False
                break
            if rematch == 'Y' or rematch == 'y':
                break
        
       
print("Its a nice Game")
