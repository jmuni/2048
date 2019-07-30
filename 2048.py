import random
import time

board =     [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

def totalscore():
    global board
    totalscore = 0
    for i in range(len(board)): #checks if any empty spaces exist
        for j in range(len(board[i])):
            totalscore += board[i][j]
    print("Score: ", totalscore)

def canup(row,col):
    global board
    if board[row-1][col] == 0 or board[row][col] == board[row-1][col]:
        return True
    else:
        return False

def candown(row,col):
    global board
    if board[row+1][col] == 0 or board[row][col] == board[row+1][col]:
        return True
    else:
        return False

def canright(row,col):
    global board
    if board[row][col+1] == 0 or board[row][col] == board[row][col+1]:
        return True
    else:
        return False

def canleft(row,col):
    global board
    if board[row][col-1] == 0 or board[row][col] == board[row][col-1]:
        return True
    else:
        return False

def fullboard(): #requires a lotta hard coding. oof
    global board
    full = True
    canMove = False
    for i in range(len(board)): #checks if any empty spaces exist
        for j in range(len(board[i])):
            if board[i][j] == 0:
                full == False
    #when full check if moves are possible
    if full:
        #corner edge checks
        #top left
        if board[0][0] == board[0][1] or board[0][0] == board[1][0]:
            canMove = True
            return False
        #top right
        if board[0][3] == board[0][2] or board[0][3] == board[1][3]:
            canMove = True
            return False
        #bot left
        if board[3][0] == board[3][1] or  board[3][0] == board[3][0]:
            canMove = True
            return False
        # bot right
        if board[3][3] == board[3][2] or board[3][3] == board[2][3]:
            canMove = True
            return False
        #edge cases here
        #top edge

        #middle cases here!
    else:
        return False


    if full and not canMove:
        return True
    else:
        return False



def printboard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] < 10:
                print(board[i][j],end ="   ")
            elif board[i][j] < 100:
                print(board[i][j], end="  ")
            elif board[i][j] < 1000:
                print(board[i][j], end=" ")
            else:
                print(board[i][j], end="")
        print("")
    totalscore()
    print("-------------")

def spawn2():
    spotfilled = True
    global board

    while spotfilled:
        row = random.randint(0,3)
        col = random.randint(0,3)

        if(board[row][col] == 0): #then spot is open
            board[row][col] = 2
            spotfilled = False


def moveup():

    global board
    moveable = False
    for count in range(3):
        for i in range(1,4): #exclude row 0
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    if board[i-1][j] == 0 or board[i - 1][j] == board[i][j]:
                    #if the spot ABOVE is 0 move up, or the SAME - combine
                        board[i-1][j] += board[i][j]
                        board[i][j] = 0
                        moveable = True
    return moveable

def movedown(): #do movable for down left and right

    global board
    moveable = False
    for count in range(3):
        for i in range(2,-1, -1): #exclude row 3, go backwards with -1 as 3rd param
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    if board[i+1][j] == 0 or board[i+1][j] == board[i][j]:
                    #if the spot BELOW is 0 - move down, or the SAME - combine
                        board[i+1][j] += board[i][j]
                        board[i][j] = 0
                        moveable = True
    return moveable

def moveleft():
    global board
    moveable = False
    for count in range(3):
        for i in range(0, 4):  # exclude col 1,
            for j in range(1,4):
                if board[i][j] != 0:
                    if board[i][j-1] == 0 or board[i][j-1] == board[i][j]:
                    # if the spot ABOVE is 0 move up, or the SAME - combine
                        board[i][j-1] += board[i][j]
                        board[i][j] = 0
                        moveable = True
    return moveable

def moveright():
    global board
    moveable = False
    for count in range(3):
        for i in range(0, 4):  # exclude col 1,
            for j in range(2,-1,-1):
                if board[i][j] != 0:
                    if board[i][j+1] == 0 or board[i][j+1] == board[i][j]:
                        # if the spot ABOVE is 0 move up, or the SAME - combine
                        board[i][j+1] += board[i][j]
                        board[i][j] = 0
                        moveable = True
    return moveable



gameover = False

#the first 2 appears on the empty board
spawn2()

while not gameover:

    printboard()

    if fullboard():
        print("You lose!")
        print("Score: ",totalscore())
        gameover = True
        exit()

    properinput = False

    while not properinput:
        keypress = input("")

        if keypress == 'w' and moveup():
                properinput = True
        elif keypress == 'a' and moveleft():
                properinput = True
        elif keypress == 's' and movedown():
                properinput = True
        elif keypress == 'd' and moveright():
                properinput = True
        else:
            print("Wrong input wasd only. Check if move is possible")

    spawn2()

