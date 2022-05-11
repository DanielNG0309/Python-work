#CPSC231 LEC01 TUT02
#NAME: Daniel Nguyen
#ID: 30102065
#DATE: October 18th 2019
#Description: This program creates a window, asks the user the coordinates of the origin and the ratio to draw the x and y axis.
#             Then it will ask the user for a funtion for it to draw on the window, circle the local maximums and minimums
#             and print out the global max and min, and the largest local max and local min onto the console

from math import *
import turtle
import sys

# CONSTANTS 
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"
DELTA=0.1
TICKLENGTH=6
YMAX= sys.float_info.max
YMIN= sys.float_info.min
#global variables for the coordinates of global maximum and global minimum
globalYMax=0
globalYMin=0
xOfGlobalYMax=0
xOfGlobalYMin=0

#
#  Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#
#  Parameters:
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x, y: the graph location to change into a screen (pixel-based) location
#
#  Usage -> screenCoor(xo, yo, ratio, 1, 0)
#
#  Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
#
def screenCoor(xo, yo, ratio, x, y):
    screenX=xo+ratio*x
    screenY=yo+ratio*y
    return screenX, screenY

# Resets the pointer location to the origin
# Parameters:
#   xo, yo : the pixel location of the origin of the  graph
#   pointer: the turtle drawing object
# Usage -> reset(pointer,xo,yo)
# Returns: Nothing
#
def reset(pointer,xo,yo):
    pointer.penup()
    pointer.goto(xo,yo)
    pointer.pendown()
    
# Makes a circle around a point on the graph
# Parameters:
#   pointer: the turtle drawing object
#   x,y: the pixel location of point on the graph
# Usage -> circle(pointer,400,300)
# Returns: Nothing
#
def circle(pointer,x,y):
    #go to a pixel location and draw a circle
    pointer.penup()
    pointer.goto(x,y-4) #4 is the radius of the circle
    pointer.pendown()
    pointer.circle(4) #4 is the radius of the circle
    #go back to its orginal position
    pointer.penup()
    pointer.goto(x,y)
    
# Finds the global ymin, lowest local ymin and circles all local ymin(s)
# Parameters:
#   pointer: the turtle drawing object
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x,y: the pixel location of a point on the graph
#   expr: the expression to draw (assumed to be valid)
#   xOfLocalYMin: the x value of the lowest local minimum of the expression
#   localYMin: the y value of the lowest local minimum of the expression
# Usage -> findYMin(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMin,localYMin)
# Returns: xOfLocalYMin,localYMin
#
def findYMin(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMin,localYMin):
    #get the y values of the point right before and right after x
    x-=DELTA
    prevY=eval(expr)
    x+=DELTA*2
    aftY=eval(expr)
    x-=DELTA #reset x to its original value
    # If y is smaller than the one right before and after it (y is a local min), this will execute
    if y<=prevY and y<=aftY:
        prevColor=pointer.pencolor()
        pointer.color("orange")
        ymin=y #ymin would then be y
        xOfLocalYMin=x
        #If ymin is smaller than global y min (y is the new global y min), this will execute
        if ymin<localYMin:
            localYMin=ymin
            xOfLocalYMin=x
            
        #converts the coordinates of the local ymins to pixel location, circle it and change the pointer's color back to normal
        screenX,screenY=screenCoor(xo,yo,ratio,x,ymin)
        circle(pointer,screenX,screenY)
        pointer.color(prevColor)
    return xOfLocalYMin,localYMin
        
# Finds the global ymax, lowest local ymax and circles all local ymax(s)
# Parameters:
#   pointer: the turtle drawing object
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x,y: the pixel location of a point on the graph
#   expr: the expression to draw (assumed to be valid)
#   xOfLocalYMax: The x value of the largest local maximum of the expression
#   localYmaxL The y value of the largest local maximum of the expression
# Usage -> findYMax(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMax,localYMax)
# Returns: xOfLocalYMax,localYMax
#
def findYMax(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMax,localYMax):
    #get the y values of the point right before and right after x
    x-=DELTA
    prevY=eval(expr)
    x+=DELTA*2
    aftY=eval(expr)
    x-=DELTA #resets x to its original value
    #if y is greater than the one right before and after it (y is a local max), this will execute
    if y>=prevY and y>=aftY:
        prevColor=pointer.pencolor()
        pointer.color("purple")
        ymax=y #ymax would then be y
        #if ymax is greater than global ymax (ymax is the new global ynax), this will execute
        if ymax>localYMax:
            localYMax=ymax
            xOfLocalYMax=x
        #converts the coordinates of the local ymaxes to pixel location, circle it and change the pointer's color back to normal
        screenX,screenY=screenCoor(xo,yo,ratio,x,ymax)
        circle(pointer,screenX,screenY)
        pointer.color(prevColor)
    return xOfLocalYMax,localYMax
    


#
#  Returns a string of the colour to use for the current expression being drawn
#  This colour is chosen based on which how many expression have previously been drawn
#  The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
#  then loops back to red, then green, then blue, again
#
#  Usage -> getColor(counter)
#
#  Parameters:
#  counter: an integer where the value is a count (starting at 0) of the expressions drawn
#
#  Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.
#
def getColor(counter):
    if counter%3==0:
        color="red"
    elif counter%3==1:
        color="green"
    else:
        color="blue"
        
    return color

#
#  Draw in the window an xaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawXAxisLabelTick(pointer, screenX, screenY, text):
    #draws ticks on the x axis
    pointer.goto(screenX,screenY+TICKLENGTH/2)
    pointer.goto(screenX,screenY-TICKLENGTH/2)
    pointer.penup()
    #write the labels on the x axis
    pointer.goto(screenX-5,screenY-15) #this is to format the label to an appropriate position
    pointer.write(text,align="left",font=("Arial",6,"bold"))
    pointer.goto(screenX,screenY)
    pointer.pendown()
    pass

#
#  Draw in the window an yaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawYAxisLabelTick(pointer, screenX, screenY, text):
    #draw ticks on the y axis
    pointer.goto(screenX+TICKLENGTH,screenY)
    pointer.goto(screenX-TICKLENGTH,screenY)
    pointer.penup()
    #writes the labels on the y axis
    pointer.goto(screenX-15,screenY-6) #this is to format the label to an appropriate position
    pointer.write(text,align="left",font=("Arial",6,"bold"))
    pointer.goto(screenX,screenY)
    pointer.pendown()
    pass

#
#  Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
#
#  Usage -> drawXAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
#
def drawXAxis(pointer, xo, yo, ratio):
    xmin=xmax=0
    reset(pointer,xo,yo)
    #while the x coordinate of the pointer is less than WIDTH(800), this will loop
    while pointer.xcor()<WIDTH:
        xmax+=1
        screenX,screenY=screenCoor(xo,yo,ratio,xmax,0)
        pointer.goto(screenX,screenY)
        drawXAxisLabelTick(pointer,screenX,screenY,str(xmax))
    reset(pointer,xo,yo)
    #while the x coordinate of the pointer is greater than 0 (the boundary), this will loop
    while pointer.xcor()>0:
        xmin-=1
        screenX,screenY=screenCoor(xo,yo,ratio,xmin,0)
        pointer.goto(screenX,screenY)
        drawXAxisLabelTick(pointer,screenX,screenY,str(xmin))
    return xmin, xmax

#
#  Draw in the window an yaxis 
#
#  Usage -> drawYAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: nothing
#
def drawYAxis(pointer, xo, yo, ratio):
    ymin=ymax=0
    reset(pointer,xo,yo)
    #while the x coordinate of the pointer is less than HEIGHT(600), this will loop
    while pointer.ycor()<HEIGHT:
        ymax+=1
        screenX,screenY=screenCoor(xo,yo,ratio,0,ymax)
        pointer.goto(screenX,screenY)
        drawYAxisLabelTick(pointer,screenX,screenY,str(ymax))
    reset(pointer,xo,yo)
    #while the x coordinate of the pointer is greater than 0 (the boundary), this will loop
    while pointer.ycor()>0:
        ymin-=1
        screenX,screenY=screenCoor(xo,yo,ratio,0,ymin)
        pointer.goto(screenX,screenY)
        drawYAxisLabelTick(pointer,screenX,screenY,str(ymin))
    #sets up the default value of globalYMin and globalYMax
    global globalYMin,globalYMax
    globalYMin=YMAX
    globalYMax=YMIN

#
#  Draw in the window the given expression (expr) between [xmin, xmax] graph locations
#
#  Usage -> drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  expr: the expression to draw (assumed to be valid)
#  xmin, ymin : the range for which to draw the expression [xmin, xmax]
#
#  Returns: Nothing
#
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    #sets up the default value for localYMin,localYMax, xOfLocalYMin, xOfLocalYMax and the start of x
    global globalYMax,globalYMin,xOfGlobalYMax,xOfGlobalYMin
    localYMin=YMAX
    localYMax=YMIN
    xOfLocalYMin=xOfLocalYMax=0
    x=xmin
    pointer.penup()
    
    #while x is still in the range, this will loop
    while xmin<=x<=xmax:
        y=eval(expr)
        screenX,screenY=screenCoor(xo,yo,ratio,x,y)
        pointer.goto(screenX,screenY)
        #get the coordinates of the largest local maximum and the lowest local minimum to print and compare with global maximum and minimum
        xOfLocalYMin,localYMin=findYMin(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMin,localYMin)
        xOfLocalYMax,localYMax=findYMax(pointer,x,y,expr,xo,yo,ratio,xOfLocalYMax,localYMax)
        pointer.pendown()
        x+=DELTA
    #if localYMin is lower than globalYMin, this will execute to update it
    if localYMin<=globalYMin:
        globalYMin=localYMin
        xOfGlobalYMin=xOfLocalYMin
    #if localYMax is greater than globalYMax, this will execute to update it
    if localYMax>=globalYMax:
        globalYMax=localYMax
        xOfGlobalYMax=xOfLocalYMax
        
    #this will execute if the largest local ymax still has it default value (no largest local ymax)
    if localYMax==YMIN:                         
        print("\nNo largest local maximum")
    else:
        print("\nLargest local maximum ({0:.5f},{1:.5f})".format(xOfLocalYMax,localYMax))
     #this will execute if the lowest local ymin still has it default value (no lowest local ymin)
    if localYMin==YMAX:                          
        print("No largest local minimum")
    else:                        
        print("Lowest local minimum ({0:.5f},{1:.5f})".format(xOfLocalYMin,localYMin))
            
     #this will execute if the global ymax still has it default value (no global ymax)
    if globalYMax==YMIN:                            
        print("No global maximum")
    else:
        print("Global maximun ({0:.5f},{1:.5f})".format(xOfGlobalYMax,globalYMax))
            
    #this will execute if the global ymin still has it default value (no global ymin)
    if globalYMin==YMAX:                            
        print("No global minimum\n")
    else:
        print("Global minimum ({0:.5f},{1:.5f})\n".format(xOfGlobalYMin,globalYMin))
#
#  Setup of turtle screen before we draw
#  
#
#  Returns: pointer
#
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    pointer.pensize(2)
    pointer.speed("fastest")
    screen.delay(delay=0)
    return pointer

#
#  Main function that attempts to graph a number of expressions entered by the user
#  The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
#  Circles the local ymin(s) and local ymax(s)
#  Prints back to the console largest local ymax, lowest local ymin, global ymax and global ymin
#  The window size is always 800 width by 600 height in pixels
#
#
#  Returns: Nothing
#
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw experssions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    #while the user does not want to exit, this will keep looping
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1
 
#Run the program
main()
