# Hello welcome to my TIC-TAC-TOE Game...

Progamming language used python3

To open server
```
python3 ttt.py -server 
```
To open clinet
```
python3 ttt.py -client 
```

# Using common board on client and server 
I used prettytable library from python to create this table design

!<img width="138" alt="Screenshot 2023-04-16 at 3 25 57 PM" src="https://media.github.khoury.northeastern.edu/user/13970/files/6eb85cce-dafc-492a-8566-ee48349eaca3">

Asking server and client to choose 'X' or 'O'

```
what do you want to choose X or O : O
```

Players were able to change turns when they enter there respective 'X' or 'O'

<img width="956" alt="Screenshot 2023-04-16 at 3 37 06 PM" src="https://media.github.khoury.northeastern.edu/user/13970/files/325bbb20-2f7b-44d6-974f-e236ea2e0310">


# Declaring a winner

The functions.checkWin() function checks every row and column and two diagnols to deceide the winner

<img width="1052" alt="Screenshot 2023-04-16 at 3 44 22 PM" src="https://media.github.khoury.northeastern.edu/user/13970/files/d56b3ab4-7887-46d1-8630-41c6c933d2c2">

# Resetting Game Environment

If either of the player wins, then system verifys their interest to Re-Match.

<img width="1055" alt="Screenshot 2023-04-16 at 3 49 09 PM" src="https://media.github.khoury.northeastern.edu/user/13970/files/9a847b61-4f3a-458b-b31f-111bb263f045">

# Closing the Game

Players can close game when either of the player WON the MATCH or Match is Tied, By typing 'N' users can close the game.

<img width="1142" alt="Screenshot 2023-04-16 at 5 11 39 PM" src="https://media.github.khoury.northeastern.edu/user/13970/files/bffb0811-ec0d-418c-b1f5-1be2733d771e">


