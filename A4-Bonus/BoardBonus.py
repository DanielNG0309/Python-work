#CPSC231 LEC01 TUT02
#NAME: Daniel Nguyen
#ID: 30102065
#DATE: December 6th 2019
#DESCRIPTION: This file creates a class(bonus) for the board of the tic tac toe game with all needed modules like: full,won,canPlay,...


#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:

    # This will create the constructor to create a 2d list with the indicated rows and columns
    # Usage -> Will be used everytime the class Board is called
    # Parameters:
    #           +self: the object (Board) itself
    #           +rows: the number of rows in the board (2d list)
    #           +cols: the number of columns in the board
    # Return: None
    def __init__(self,rows=3,cols=3):
        #creates empty list
        self.board=[]
        #this will loop through every row of the board
        for row in range(rows):
            #appending the rows of empty slots (the value of empty is 0) into the board according to the number of rows
            self.board.append([EMPTY] * cols)

    # This will get the number of rows in the board
    # Usage -> self.rows()
    # Parameters: self which is the object (Board) itself
    # Return: the length of the board which is the number of rows
    def rows(self):
        return len(self.board)
    
    # This will get the number of columns in the board
    # Usage -> self.cols()
    # Parameters: self which is the object (Board) itself
    # Return: the length of the first key at index 0 (also a list) in the 2d list board which is the number of colums
    def cols(self):
        return len(self.board[0])
    
    # This will determine if a player/computer can play on a slot or not
    # Usage -> self.canPlay(row,col)
    # Parameters:
    #           +self: the object (Board) itself
    #           +row: the row to play in the board 
    #           +col: the column to play in the board
    # Return: whether or not the slot is playable
    def canPlay(self,row,col):
        #If the slot is not occupied, return true
        if self.board[row][col]==EMPTY:
            return True
        #If it not empty then return false
        else:
            return False
        
    # This will put a piece of the player/computer into a slot
    # Usage -> self.play(row,col,piece)
    # Parameters:
    #           +self: the object (Board) itself
    #           +row: the row to play in the board 
    #           +col: the column to play in the board
    #           +piece: X or O piece to put into the board, indicating one's play
    # Return: None
    def play(self,row,col,piece):
        #put the piece into the exact row and column
        self.board[row][col]=piece
        
    # This will determine if the board is full or not
    # Usage -> self.full()
    # Parameters: None
    # Return: whether or not the board is full              
    def full(self):
        #Loop through each row in the board
        for row in self.board:
            #Loop through each slot in a row
            for slot in row:
                #If the slot is empty then the board is not full
                if slot==EMPTY:
                    return False
        #If none is empty the board is full
        return True

    # This will determine if a player/computer has won in a row
    # Usage -> self.winInRow(row,piece,win)
    # Parameters:
    #           +self which is the object (Board) itself
    #           +row: the row to play in the board 
    #           +piece: X or O piece to put into the board, indicating one's play
    #           +win: how many pieces needed in a pattern to win
    # Return: whether or not a player/computer has won in a row
    def winInRow(self,row,piece,win):
        #Loop through every columns of the row (slots)
        for col in range(self.cols()):
            
            #when win condition is 3, this will execute
            if win=="3":
                #If there is three consecutives slots in a row is within the board, this will execute
                if col+2 in range(self.cols()):
                    #If three consecutives piece of the same kind has been played on a row, return true
                    if self.board[row][col]==piece:
                        if self.board[row][col+1]==piece:
                            if self.board[row][col+2]==piece:
                                return True
                            
            #when win condition is 4, this will execute
            if win=="4":
                #If there is 4 consecutives slots in a row is within the board, this will execute
                if col+3 in range(self.cols()):
                    #If 4 consecutives piece of the same kind has been played on a row, return true
                    if self.board[row][col]==piece:
                        if self.board[row][col+1]==piece:
                            if self.board[row][col+2]==piece:
                                if self.board[row][col+3]==piece:
                                    return True
                                
            #when win condition is 5, this will execute
            if win=="5":
                #If there is 5 consecutives slots in a row is within the board, this will execute
                if col+4 in range(self.cols()):
                    #If 5 consecutives piece of the same kind has been played on a row, return true
                    if self.board[row][col]==piece:
                        if self.board[row][col+1]==piece:
                            if self.board[row][col+2]==piece:
                                if self.board[row][col+3]==piece:
                                    if self.board[row][col+4]==piece:
                                        return True
                
        #If the loop goes through every single slots and has not find 3 consecutives pieces, there would be no win in that row so return false
        return False
    
    # This will determine if a player/computer has won in a column
    # Usage -> self.winInCol(col,piece,win)
    # Parameters:
    #           +self which is the object (Board) itself
    #           +col: the column to play in the board
    #           +piece: X or O piece to put into the board, indicating one's play
    #           +win: how many pieces needed in a pattern to win
    # Return: whether or not a player/computer has won in a column
    def winInCol(self,col,piece,win):
        #Loop through every rows of the column (slots)
        for row in range(self.rows()):

            #When the win condition is 3, this will execute
            if win=="3":
                #If there is three consecutives slots in a column is within the board, this will execute
                if row+2 in range(self.rows()):
                    #If three consecutives piece of the same kind has been played in a column, return true
                    if self.board[row][col]==piece:
                        if self.board[row+1][col]==piece:
                            if self.board[row+2][col]==piece:
                                return True
                            
            #When the win condition is 4, this will execute
            if win=="4":
                #If there is 4 consecutives slots in a column is within the board, this will execute
                if row+3 in range(self.rows()):
                    #If 4 consecutives piece of the same kind has been played in a column, return true
                    if self.board[row][col]==piece:
                        if self.board[row+1][col]==piece:
                            if self.board[row+2][col]==piece:
                                if self.board[row+3][col]==piece:
                                    return True

            #When the win condition is 5, this will execute
            if win=="5":
                #If there is 5 consecutives slots in a column is within the board, this will execute
                if row+4 in range(self.rows()):
                    #If 5 consecutives piece of the same kind has been played in a column, return true
                    if self.board[row][col]==piece:
                        if self.board[row+1][col]==piece:
                            if self.board[row+2][col]==piece:
                                if self.board[row+3][col]==piece:
                                    if self.board[row+4][col]==piece:
                                        return True
                    
        #If the loop goes through every single slots and has not find 3 consecutives pieces, there would be no win in that column so return false
        return False
    
    # This will determine if a player/computer has won in any diagonals
    # Usage -> self.winInDiag(piece,win)
    # Parameters:
    #           +self which is the object (Board) itself
    #           +piece: X or O piece to put into the board, indicating one's play
    #           +win: how many pieces needed in a pattern to win
    # Return: whether or not a player/computer has won in any diagonals
    def winInDiag(self,piece,win):
        #Loop through every rows and colums of the board
        for row in range(self.rows()):
            for col in range(self.cols()):

                #If a piece is played on the board, this will execute
                if self.board[row][col]==piece:

                    #When the win condition is 3, this will execute
                    if win=="3":
                        #If the three consecutives foward diagonal slots is within the board, this will execute
                        if row+2 in range(self.rows()) and col+2 in range(self.cols()):
                            #If there is a foward diagonal win, return true
                            if self.board[row+1][col+1]==piece:
                                if self.board[row+2][col+2]==piece:
                                    return True
                            
                        #If the three consecutives reverse diagonal slots is within the board, this will execute
                        elif row+2 in range(self.rows()) and col-2 in range(self.cols()):
                            #If there is a reverse diagonal win, return true
                            if self.board[row+1][col-1]==piece:
                                if self.board[row+2][col-2]==piece:
                                    return True
                                
                    #When the win condition is 4, this will execute
                    if win=="4":
                        #If the 4 consecutives foward diagonal slots is within the board, this will execute
                        if row+3 in range(self.rows()) and col+3 in range(self.cols()):
                            #If there is a foward diagonal win, return true
                            if self.board[row+1][col+1]==piece:
                                if self.board[row+2][col+2]==piece:
                                    if self.board[row+3][col+3]==piece:
                                        return True
                            
                        #If the 4 consecutives reverse diagonal slots is within the board, this will execute
                        elif row+3 in range(self.rows()) and col-3 in range(self.cols()):
                            #If there is a reverse diagonal win, return true
                            if self.board[row+1][col-1]==piece:
                                if self.board[row+2][col-2]==piece:
                                    if self.board[row+3][col-3]==piece:
                                        return True

                    #When the win condition is 5, this will execute
                    if win=="5":
                        #If the 5 consecutives foward diagonal slots is within the board, this will execute
                        if row+4 in range(self.rows()) and col+4 in range(self.cols()):
                            #If there is a foward diagonal win, return true
                            if self.board[row+1][col+1]==piece:
                                if self.board[row+2][col+2]==piece:
                                    if self.board[row+3][col+3]==piece:
                                        if self.board[row+4][col+4]==piece:
                                            return True
                            
                        #If the 5 consecutives reverse diagonal slots is within the board, this will execute
                        elif row+4 in range(self.rows()) and col-4 in range(self.cols()):
                            #If there is a reverse diagonal win, return true
                            if self.board[row+1][col-1]==piece:
                                if self.board[row+2][col-2]==piece:
                                    if self.board[row+3][col-3]==piece:
                                        if self.board[row+4][col-4]==piece:
                                            return True
                            
        #If the loop goes through every single slots and has not find 3 consecutives pieces, there would be no win in any diagonals so return false    
        return False
    
    # This will determine if a player/computer has won the game
    # Usage -> self.won(piece,win)
    # Parameters:
    #           +self which is the object (Board) itself
    #           +piece: X or O piece to put into the board, indicating one's play
    #           +win: how many pieces needed in a pattern to win
    # Return: whether or not a player/computer has won the game       
    def won(self, piece,win):
        #Loop through every rows of the board
        for row in range(self.rows()):
            #If one has won in a row, return true
            if self.winInRow(row,piece,win):
                return True

        #Loop through every colums of the board
        for col in range(self.cols()):
            #If one has won in a column, return true
            if self.winInCol(col,piece,win):
                return True
        #If there is a diagonal win, return true
        if self.winInDiag(piece,win):
            return True

        #If no win condition is met, return false
        return False

    # This will give the player some hints
    # Usage -> self.hint(piece,win)
    # Parameters:
    #           +self which is the object (Board) itself
    #           +piece: X or O piece to put into the board, indicating one's play
    #           +win: how many pieces needed in a pattern to win
    # Return: the suggested row and column to play          
    def hint(self, piece,win):
        #Loop through all rows and columns of the board
        for row in range(self.rows()):
            for col in range(self.cols()):
                
                #If the slot is playable, play the piece
                if self.canPlay(row,col):
                    self.play(row,col,piece)
                    
                    #If player would win with that play, empty that slot and return the row and column
                    if self.won(piece,win):
                        self.board[row][col]=EMPTY
                        return row,col
                    #If not then just empty the slot
                    else:
                        self.board[row][col]=EMPTY
                        
        #The default if no hint is able to be given
        return -1, -1
    
    # This will determine if the game is over or not
    # Usage -> self.gameover(win)
    # Parameters: win: how many pieces needed in a pattern to win
    # Return: whether or not the game is over  
    def gameover(self,win):
        #If X or O has won or the board is full, return true
        if self.won(X,win) or self.won(O,win) or self.full():
            return True
        #If not, return false
        return False

    


