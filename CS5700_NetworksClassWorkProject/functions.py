import numpy as np
from prettytable import PrettyTable

board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
def modifyTable(board):
    table = PrettyTable(['', '1', '2', '3'])
    for i in range(3):
        table.add_row([str(i+1)] + list(board[i]))
    return table

def checkWin(arr,sybl):
    if arr[0][0] == sybl and arr[0][1] == sybl and arr[0][2] == sybl: #row 1
        return True
    if arr[1][0] == sybl and arr[1][1] == sybl and arr[1][2] == sybl: #row 2
        return True
    if arr[2][0] == sybl and arr[2][1] == sybl and arr[2][2] == sybl: #row 3
        return True
    if arr[0][0] == sybl and arr[1][1] == sybl and arr[2][2] == sybl: #Dig 1
        return True
    if arr[0][2] == sybl and arr[1][1] == sybl and arr[2][0] == sybl: #Dig 2
        return True
    if arr[0][0] == sybl and arr[1][0] == sybl and arr[2][0] == sybl: #Clm 1
        return True
    if arr[0][1] == sybl and arr[1][1] == sybl and arr[2][1] == sybl: #clm 2
        return True
    if arr[0][2] == sybl and arr[1][2] == sybl and arr[2][2] == sybl: #clm 3
        return True
    else:return False

def checkTie(arr,sybl):
    if(checkWin(arr,sybl) == False):
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != ' ':
                    count += 1
        if(count == 9):
            return True
        else:
            return False
    else:
        return False

def checkEmptyElement(arr,row,clm):
    if arr[row-1][clm-1] == ' ':
        return True
    else:
        return False