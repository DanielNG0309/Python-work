# Python-work
All works with Python from CPSC 231

### Description
#### Assignment 1
This program creates a window with x and y axis using Turtle, asks inputs from the user to draw a circle and line(s), and then calculates and circles the intersection(s)
#### Assignment 2
This program creates a window, asks the user the coordinates of the origin and the ratio to draw the x and y axis.

Then it will ask the user for a funtion for it to draw on the window, circle the local maximums and minimums and print out the global max and min, and the largest local max and local min onto the console

#### Assignment 3
This program plots stars and constellations with its names and bounding boxes from input files and then outputs all named stars with its values, the names of the stars in a constellation with its values onto the python shell, and the xmin,xmax,ymin,ymax values of a constellation into a file
#### Assignment 4
This program is a 1 player tictactoe game (user vs computer) with adjustable dimensions, difficulty and hint option

Usage: "python tictactoe.py rows cols difficulty piece (optional)-h or -a".

The bonus part of this assignment is to include another argument deciding how many pieces needed to play in a row, collumn or diagonal for the player or computer to win

Usage: "python tictactoe.py rows cols difficulty piece win (optional)-h or -a".

  Where:
  
         rows and cols are the number of rows and collums of the game board (in range [3:5])
  
         difficulty is from 0 (minimum) and 4 (maximum)
  
         piece is for the user to choose either "X" or "O" (X goes first)
         
         win determine how many pieces needed to be placed to win (in range [3:5] and possible within the dimensions of the board)
  
         the optional argument "-h" or "-a" is for the hint move recommended by the computer that is depicted in orange (-h = basic hint, -a = advanced hint)
         
         
The algorithms for error check, hints, and the computer's move according to the chosen difficulty was written by my instructor. The rest was written by me.
