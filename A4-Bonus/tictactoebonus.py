from SimpleGraphics import *
from random import shuffle
from math import factorial
from copy import deepcopy
import inspect
import sys
from pprint import pprint
import traceback
from BoardBonus import Board, X, O, EMPTY

# Contants for the board size
WIDTH = 600
HEIGHT = 600

##############################################################################
##
##  Code for drawing (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

# Draw X with lines in box beginning at (x,y) with given square size and color
def drawX(x, y, size, color="black"):
    setColor(color)
    line(x+15,y+15,x+size-15,y+size-15)
    line(x+size-15,y+15,x+15,y+size-15)

# Draw O with lines in box beginning at (x,y) with given square size and color    
def drawO(x, y, size, color="black"):
    setColor(color)
    setFill(None)
    ellipse(x+15,y+15,size-30,size-30)

# Draw hint information and X or O based on piece in given row, col of board
def drawHint(board, row, col, piece):
    setColor("orange")
    setFill(None)
    rows = board.rows()
    cols = board.cols()
    row_diff = int(HEIGHT/rows)
    col_diff = int(WIDTH/cols)
    rect(col*col_diff,row*row_diff,row_diff+1,col_diff+1)
    if piece == X:
        drawX(col*col_diff,row*row_diff,min(row_diff,col_diff), "orange")
    elif piece == O:
        drawO(col*col_diff,row*row_diff,min(row_diff,col_diff), "orange")

# Draw the board in given color
def drawBoard(board, color="black"):
    setColor("white")
    rect(0,0,WIDTH,HEIGHT)
    setColor(color)
    rows = board.rows()
    cols = board.cols()
    row_diff = int(HEIGHT/rows)
    col_diff = int(WIDTH/cols)
    for y in range(row_diff,HEIGHT-1,row_diff):
        line(0,y,WIDTH,y)
    for x in range(col_diff,WIDTH-1,col_diff):
        line(x,0,x,HEIGHT)
    for row in range(board.rows()):
        for col in range(board.cols()):
            if board.board[row][col] == X:
                drawX(col*col_diff,row*row_diff,min(row_diff,col_diff), color)
            elif board.board[row][col] == O:
                drawO(col*col_diff,row*row_diff,min(row_diff,col_diff), color)

#Setup window and draw initial white line to make it resize
def setupWindow():
    background("white")
    setColor("white")
    resize(WIDTH,HEIGHT)
    line(0,0,1,1)    

##############################################################################
##
##  Code for AI and hint for 3x3 tic-tac-toe (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

#Main minmax, calls subfunction for recursion
#uses game board with player1 trying to decide move vs player 2, limit to depth given
def minmax1(board, player1, player2, depth,win):
    #Find all valid moves, shuffle for interesting
    moves = []
    rows = list(range(0,board.rows()))
    shuffle(rows)
    cols = list(range(0,board.cols()))
    shuffle(cols)
    for row in rows:
        for col in cols:
            if board.canPlay(row, col):
                moves.append([row,col])
    values = []
    #for each move if game won save value (make bigger than regular to show next play wins)
    #if not won recurse on game state for opponent playing
    for move in moves:
        row = move[0]
        col = move[1]
        board.play(row,col,player1)
        if board.won(player1,win):
            values.append(20)
        elif board.won(player2,win):
            values.append(-20)
        elif board.full():
            values.append(0)
        else:
            values.append(minmax2(board, player1, player2, False, depth-1,win))
        board.play(row,col,EMPTY)
    #Return best move found, next play wins first, followed by future wins, and ties, losses, and next play losses
    for i in range(len(moves)):
        if values[i] == 20:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == 10:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == 0:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == -10:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == -20:
            return moves[i][0], moves[i][1]
    return -1, -1
        
#Recursion minmax, calls itself for recursion
#uses game board with player1 trying to decide move vs player 2, limit to depth given
#not of maximze means it is player1's turn and not maximize is player2's turn
def minmax2(board, player1, player2, maximize, depth,win):
    if depth == 0:
        return 0
    #Find all valid moves, shuffle for interesting
    moves = []
    rows = list(range(0,board.rows()))
    shuffle(rows)
    cols = list(range(0,board.cols()))
    shuffle(cols)
    for row in rows:
        for col in cols:
            if board.canPlay(row, col):
                moves.append([row,col])
    values = [] 
    #for each move if game won save value
    #if not won recurse on game state for opponent playing
    for move in moves:
        row = move[0]
        col = move[1]
        if maximize:
            board.play(row,col,player1)
        else:
            board.play(row,col,player2)
        if board.gameover(win):
            if board.won( player1,win):
                board.play(row,col,EMPTY)
                return 10
            elif board.won( player2,win):
                board.play(row,col,EMPTY)
                return -10
            elif board.full():
                board.play(row,col,EMPTY)
                return 0
        result = minmax2(board, player1, player2, not maximize, depth-1,win)
        values.append(result)
        if maximize and result == 10:
            board.play(row,col,EMPTY)
            break
        elif not maximize and result == -10:
            board.play(row,col,EMPTY)
            break
        board.play(row,col,EMPTY)
    #Return maximial or minimal value found depending on recursion level
    if len(values) == 0:
        return 0
    if maximize:
        return max(values)
    else:
        return min(values)

#Calling AI, if level 4 we do full recursive minmax, if not we recurse only to certain depth
#If level=0 AI we just pick random open spot
def AI(board, level, human, computer,win):
    if level == 4:
        return minmax1(board, computer, human, board.rows()*board.cols()+1,win)
    elif level > 0 :
        return minmax1(board, computer, human, level*2,win)
    rows = list(range(0,board.rows()))
    shuffle(rows)
    cols = list(range(0,board.cols()))
    shuffle(cols)
    trying = True
    for row in rows:
        for col in cols:
            if board.canPlay( row, col):
                return row, col
    return -1, -1
 
##############################################################################
##
##  Main function (IF YOU ARE READING THIS YOU BETTER NOT BE CHANGING CODE DOWN HERE)
##
##############################################################################

def main():
    rows = None
    cols = None
    difficulty = None
    human = None
    computer = None
    hint = None
    if not checkArgs(sys.argv):
        sys.exit(1)
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    difficulty = int(sys.argv[3])
    piece = sys.argv[4]
    win=sys.argv[5]
    if piece == "X":
        print("Human is X.")
        print("Computer is O.")
        human = X
        computer = O
    else:
        print("Human is O.")
        print("Computer is X.")
        human = O
        computer = X
    if(len(sys.argv) == 7):
        if sys.argv[6] == "-a":
            hint = "adv"
        else:
            hint = "hint"
    setupWindow()
    board = Board(rows,cols)
    drawBoard(board)
    player = X
    plays = 0
    while not board.gameover(win):
        value = (rows*cols)-plays
        if(value > 0):
            complexity = factorial(value)
            print("Estimated complexity of current game:",complexity)
        if human == player:
            print("Human player's turn.")
            if hint == "hint":
                row1, col1 = board.hint(human,win)
                row2, col2 = board.hint(computer,win)
                if row1 != -1:
                    print("Hint is row =",row1,"and col =",col1)
                    drawHint(board, row1,col1,human)
                elif row2 != -1:
                    print("Hint is row =",row2,"and col =",col2)
                    drawHint(board, row2,col2,human)
                else:
                    print("No hint")
            elif hint == "adv":
                row = -1
                col = -1
                if rows == cols == 3:
                    row, col = minmax1(board, human, computer, 5,win)
                else:
                    row, col = minmax1(board, human, computer, 4,win)
                if row != -1:
                    print("Hint is row =",row,"and col =",col)
                    drawHint(board, row,col,human)
                else:
                    print("No hint")

            trying = True
            while trying:
                selection = list(range(0,rows))
                row = -1
                while row < 0 or row > rows-1:
                    try:
                        row = int(input("Enter row "+str(selection)+": "))
                    except Exception as e:
                        print("Invalid row entered!")    
                selection = list(range(0,cols))
                col = -1
                while col < 0 or col > cols-1:
                    try:
                        col = int(input("Enter col "+str(selection)+": "))
                    except Exception as e:
                        print("Invalid row entered!")
                if board.canPlay(row, col):
                    board.play(row, col, human)
                    trying = False
                else:
                    print("Chosen location board["+str(row)+"]["+str(col)+"] is full!")
                print("Human plays in row",row,"and column",str(col)+".")
                player = computer
        else:
            row, col = AI(board, difficulty, human, computer,win)
            board.play(row, col, computer)
            print("AI plays in row",row,"and column",str(col)+".")
            player = human        
        drawBoard(board)
        plays+=1
    setFont("Times", "50", "bold")

    if board.won(X,win):
        if human == X:
            drawBoard(board, "green")
        else :
            drawBoard(board, "red")
        setColor("black")
        text(300,300,"X won!")
    elif board.won(O,win):
        if human == O:
            drawBoard(board, "green")
        else :
            drawBoard(board, "red")
        setColor("black")
        text(300,300,"O won!")
    else:
        drawBoard(board, "blue")
        setColor("black")
        text(300,300,"Board full. Draw.")

def checkArgs(args):
    if(len(args) != 6 and len(args) != 7):
        print("Arguments %s"% args)
        print("Usage: python tictactoe.py <rows> <cols> <difficulty> <piece> <win> <optional -h hint -a advanced hint>")
        return False
    if not args[1].isdigit() or int(args[1]) not in [3,4,5]:
        print("Rows <%s> should be from [3,5]"%args[1])
        return False
    if not args[2].isdigit() or int(args[2]) not in [3,4,5]:
        print("Rows <%s> should be from [3,5]"%args[2])
        return False
    if (int(args[1])==int(args[2])==3):
        if not args[3].isdigit() or int(args[3]) not in [0,1,2,3,4]:
            print("Difficulty <%s> should be from [0=RANDOM,1=WINS,2=LOOKAHEAD1,3=LOOKAHEAD2,4=FULLAI]"%args[3])
            return False           
    elif not args[3].isdigit() or int(args[3]) not in [0,1,2,3]:
        print("Difficulty <%s> should be from [0=RANDOM,1=WINS,2=LOOKAHEAD1,3=LOOKAHEAD2]"%args[3])
        return False
    if args[4] != "X" and args[4] != "O":
        print("Piece <%s> should be from [X,O]"%args[4])
        return False
    if not args[5].isdigit() or int(args[5]) not in [3,4,5] or int(args[5]) > int(args[1]) and int(args[5])>int(args[2]):
        print("Invalid win condition")
        return False    
    if(len(args) == 7):
        if args[6] != "-h" and args[6] != "-a":
            print("Hint <%s> should be from [-h,-a]"%args[6])
            return False
    return True
        
main()
