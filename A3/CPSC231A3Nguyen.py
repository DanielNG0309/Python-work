#CPSC231 LEC01 TUT02
#NAME: Daniel Nguyen
#ID: 30102065
#DATE: November 15th 2019
#Description: This program plots stars and constellations with its names and bounding boxes from input files and then outputs all named stars with its values,
#   the names of the stars in a constellation with its values onto the python shell, and the xmin,xmax,ymin,ymax values of a constellation into a file

#import libraries needed
import sys
import os
import turtle

#setting up constants
WIDTH = 600
HEIGHT = 600
RATIO = 300
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"
TICK=3
PAD=5
BOXCOLOR="orange"

#   Setup of turtle screen before we draw
#   Usage -> setup()
#   Parameters: None
#   Returns: pointer
def setup():
    pointer = turtle.Turtle()
    pointer.speed("fastest")
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

#   Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#   Parameters:
#    x, y: the graph location to change into a screen (pixel-based) location
#   Usage -> screenCoor(x,y)
#
#   Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
def screenCor(x,y):
    screenX= WIDTH/2 + RATIO*x
    screenY= HEIGHT/2 +RATIO*y
    return screenX,screenY

#   Returns a string of the colour to use for the current expression being drawn
#   This colour is chosen based on which how many expression have previously been drawn
#   The counter starts at 0, the first or 0th expression, should be red, the second green, the third yellow
#   then loops back to red, then green, then yellow, again
#
#   Usage -> getColor(counter)
#
#   Parameters:
#    counter: an integer where the value is a count (starting at 0) of the expressions drawn
#
#   Returns: 0 -> "red", 1 -> "green", 2 -> "yellow", 3 -> "red", 4 -> "green", etc.
def getColor(counter):
    if counter%3==0:
        color="red"
    elif counter%3==1:
        color="green"
    else:
        color="yellow"   
    return color

#  Draw the x and y axis onto the screen
#  Usage -> drawAxes(pointer)
#  Parameters:
#   pointer: a turtle drawing object
#   Return: Nothing
def drawAxes(pointer):
    
    #set up the pointer and initial value of tick
    pointer.color(AXISCOLOR)
    tick=-1
    pointer.penup()
    pointer.goto(0,HEIGHT/2)
    pointer.pendown()

    #this will run until the pointer reaches the right side of the screen (drawing x-axis)
    while pointer.xcor()<WIDTH:
        #converts screen position to pixel location and then go to that point
        screenX,screenY=screenCor(tick,0)
        pointer.goto(screenX,screenY)
        
        #draw the label and tick (skip 0)
        if tick!=0:
            pointer.goto(screenX,screenY-TICK)
            pointer.goto(screenX,screenY+2*TICK)
            pointer.write(f'{tick:.2f}',font=("Arial",8,"bold"))
            pointer.goto(screenX,screenY)
        tick+=0.25
        
    #set tick and pointer back to its initial    
    tick=-1
    pointer.penup()
    pointer.goto(WIDTH/2,0)
    pointer.pendown()

    #this will run until the pointer reaches the top side of the screen (drawing y-axis)
    while pointer.ycor()<HEIGHT:
        screenX,screenY=screenCor(0,tick)
        pointer.goto(screenX,screenY)
        
        #draw the label and tick (skip 0)
        if tick!=0:
            pointer.goto(screenX-TICK,screenY)
            pointer.goto(screenX+2*TICK,screenY)
            pointer.write(f'{tick:.2f}',font=("Arial",8,"bold"))
            pointer.goto(screenX,screenY)
        tick+=0.25

#   Handle the command line argument depending on the cases
#   Usage -> argHandler()
#   Parameters: None
#   Return:
#    starFile which is the name of the star location file
#    nameCheck which is a boolean value determining whether or not we're going to write names on named stars
def argHandler():
    #set up the default value of name
    nameCheck=False

    # When there's no extra command line argument, this will execute
    if len(sys.argv)==1:
        starFile=input("Please enter a star location file\n>>")
        
    # When there's 2 command line arguments, this will execute
    elif len(sys.argv)==2:
        #If the second one(the first one is to run the program) is "-names" this will execute
        if sys.argv[1]=="-names":
            nameCheck=True
            starFile=input("Please enter a star location file\n>>")
        #Else (the second one this not "-names"), this will execute
        else:
            starFile=sys.argv[1]

    # When there's 3 command line arguments, this will execute
    elif len(sys.argv)==3:
        #If the third one is "-names" this will execute
        if sys.argv[2]=="-names":
            nameCheck=True
            starFile=sys.argv[1]
        #If the second one is "-names" this will execute
        elif sys.argv[1]=="-names":
            nameCheck=True
            starFile=sys.argv[2]
        #If both are not "-names", this will execute
        else:
            print("Invalid because neither input was '-names'")
            sys.exit(1)
    # When there's more than 3 command line arguments, this will execute    
    else:
        print("Too many arguments")
        sys.exit(2)
    #If the file does not exist, this will execute
    if os.path.isfile(starFile)==False:
        print("The star location file does not exist")
        sys.exit(3)
    return starFile,nameCheck

#   Read the star location file and get necessary info out of it (also prints the info about the stars in the star location file onto the python shell)
#   Usage -> readStarInfo(starFile)
#   Parameters:
#    starFile which is the name of the star location file
#   Return:
#    starTuplesList which is a list of tuples of x,y cordinate and magnitude of every star in the file
#    starInfoFull which is a dictionary of every named stars in the file with its value, including all names of the same star
#    starInfoRemoved which is a dictionary of every named stars with its value in the file with all of the extra names removed
def readStarInfo(starFile):
    #Set up the list and dictionary needed
    starTuplesList=[]
    starInfoFull={}
    
    try:
        #open the file and read it
        fileHandler= open(starFile)
        for line in fileHandler.readlines():
            #If the information in the star filename doesn’t have the required amount of entries separated by commas, this will execute
            if len(line.split(","))!=7:
                print("the information in the star filename doesn’t have the required amount of entries separated by commas")
                sys.exit(4)
            #Assigning variables to each entry
            x,y,z,id1,mag,id2,names=line.split(",")

            #If a star has a name this will execute
            if names!="\n":
                #Get the list of name(s) of a star, assign each name to its value in the dictionary
                namesList=names.strip().split(";")
                for index in range(len(namesList)):
                    starInfoFull.update({namesList[index]:(x,y,mag)})
            #Put the tuple of x,y cordinates and magnitude of a star into the list    
            starTuplesList.append((x,y,mag))

        #Get rid of names with the same values (from the same star) and put it into another dictionary by flipping the keys and values and then flip back
        #(python will automatically remove it as the keys are the same when we flip->flip back with no duplicates)
        dSwitched={value:name for name,value in starInfoFull.items()}
        starInfoRemoved={name:value for value,name in dSwitched.items()}
        #Close the file
        fileHandler.close()
        
        #print the info of named stars onto the console
        for name,value in starInfoRemoved.items():
            x,y,mag=value
            print(f"{name} is at {(float(x),float(y))} with magnitude {float(mag)}")
            
    #Account for when the file is somehow not accesible        
    except OSError:
        print("Cannot open/read file")
        sys.exit(5)
    #Accounts for when the info in the file is of the wrong type
    except ValueError:
        print("The information in the file is of the wrong type")
        sys.exit(6)
    #Account for unexpected errors
    except:
        print("Unexpected error")
        sys.exit(7)
    return starTuplesList,starInfoFull,starInfoRemoved

#   Draw all named stars in white and the rest in grey
#   Parameters
#    pointer: the turtle drawing object
#    starTuplesList: the list of tuples of x,y cordinate and magnitude of every star in the file
#    StarInfoRemoved: a dictionary of every named stars with its value in the file with all of the extra names removed
#    nameCheck: a boolean value determining whether or not we're going to write names on named stars
#   Usage -> drawStars(pointer,starTuplesList,starInfoRemoved,nameCheck)
#   Return: Nothing
def drawStars(pointer,starTuplesList,starInfoRemoved,nameCheck):
    pointer.color(STARCOLOR2)
    #draw all stars in the star location file until all info in the list is read
    for starInfo in starTuplesList:
        #set up needed variables
        x,y,mag=starInfo
        radius=(10/(float(mag)+2))/2
        pointer.penup()
        pointer.goto(screenCor(float(x),float(y)))
        #draw filled circle for stars
        pointer.pendown()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
        pointer.penup()
        
    pointer.color(STARCOLOR)
    #draw all named stars
    for key,values in starInfoRemoved.items():
        #set up needed variables
        x,y,mag=values
        radius=(10/(float(mag)+2))/2
        pointer.goto(screenCor(float(x),float(y)))
        #draw filled circle for stars
        pointer.pendown()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
        #if nameCheck is true, this will execute
        if nameCheck:
            pointer.write(key,font=("Arial", 5, "normal"))
        pointer.penup()
        
#   Read the constellation file and get necessary info from it (also prints the info about the stars in the constellation file onto the python shell)
#   Parameter: constell: the name of the constellation file
#   Usage -> readConstellInfo(constell)
#   Return:
#    starNamesList which is a list of names of the edges of the constellation
#    constellName which is the name of the constellation 
def readConstellInfo(constell):
    #Set up the list and dictionary needed
    starNamesList=[]
    starsInConstell=[]
    try:
        #open the file and read it
        fileHandler=open(constell)
        #get the first line of file (name of constellation)
        constellName=fileHandler.readline().strip("\n")
        #read the rest
        for line in fileHandler.readlines():
            edges=line.strip().split(",")
            #If the information in the file have the required amount of entries separated by commas, this will execute
            if len(edges)==2:
                starNamesList.append(edges)
            #If not, this will execute
            else:
                print("the information in the file doesn’t have the required amount of entries separated by commas\n")
                sys.exit(8)
        #close the file
        fileHandler.close()

        #print the info of the stars in the constellation onto the console
        for names in starNamesList:
            starsInConstell.append(names[0])
        print(f"{constellName} contains {set(starsInConstell)}\n")
        
    #Account for when the file is somehow not accesible  
    except OSError:
        print("Cannot open/read file")
        sys.exit(9)
    #Account for unexpected errors
    except:
        print("Unexpected error")
        sys.exit(10)
    
    return starNamesList,constellName

#   Draw the constellation and store its edges info
#   Parameters:
#    pointer: the turtle drawing object
#    starNamesList: a list of names of the edges of the constellation
#    starInfoFull: a dictionary of every named stars in the file with its value, including all names of the same star
#   Return:
#    edgesXCoorList which is the list of x coordinates of the edges of the constellation
#    edgesYCoorList which is the list of y coordinates of the edges of the constellation 
def drawConstellation(pointer,starNamesList,starInfoFull):
    #set up needed dictionaries
    edgesXCoorList=[]
    edgesYCoorList=[]
    
    #draw the constellation until all the the info in the list is read
    for names in starNamesList:
        #get the keys from the list and then use it to access the x and y values of the stars
        name1,name2=names
        x1,y1,_=starInfoFull[name1]
        x2,y2,_=starInfoFull[name2]
        #draw an edge of the constellation
        pointer.goto(screenCor(float(x1),float(y1)))
        pointer.pendown()
        pointer.goto(screenCor(float(x2),float(y2)))
        pointer.penup()
        #update the x and y values to the according list
        edgesXCoorList.extend([float(x1),float(x2)])
        edgesYCoorList.extend([float(y1),float(y2)])
    return edgesXCoorList,edgesYCoorList

#   Draw the bounding box of the constellation with its name (also output the xmin,xmax,ymin,ymax into a file)
#   Parameters:
#    pointer: the turtle drawing object
#    edgesXCoorList: the list of x coordinates of the edges of the constellation
#    edgesYCoorList: the list of y coordinates of the edges of the constellation
#    constellName: the name of the constellation
#   Usage -> drawBoundBox(pointer,edgesXCoorList,edgesYCoorList,constellName)
#   Return: Nothing
def drawBoundBox(pointer,edgesXCoorList,edgesYCoorList,constellName):
    #get the xmax,xmin,ymax,ymin from the list
    xmax=max(edgesXCoorList)
    xmin=min(edgesXCoorList)
    ymax=max(edgesYCoorList)
    ymin=min(edgesYCoorList)
    #convert screen locations into pixel locations 
    screenXMax,screenYMax=screenCor(xmax,ymax)
    screenXMin,screenYMin=screenCor(xmin,ymin)

    pointer.color(BOXCOLOR)
    #draw the bounding box of the constellation with padding
    pointer.goto(screenXMin-PAD,screenYMin-PAD)
    pointer.pendown()
    pointer.goto(screenXMax+PAD,screenYMin-PAD)
    pointer.goto(screenXMax+PAD,screenYMax+PAD)
    pointer.goto(screenXMin-PAD,screenYMax+PAD)
    pointer.goto(screenXMin-PAD,screenYMin-PAD)
    pointer.penup()
    #get to the center of the top edge of the box to draw the name of the constellation
    pointer.goto((screenXMax+PAD+screenXMin+PAD)/2,(screenYMax+PAD))
    pointer.write(constellName,align="center",font=("Arial",7,"normal"))

    #create an output file and put xmin,xmax,ymin,ymax in it
    fileHandler= open(constellName+"_box.dat","w+")
    fileHandler.write(f'''{xmin}
{xmax}
{ymin}
{ymax}''')
    #close the file
    fileHandler.close()
    
#   The main funtion attempts to plot stars and constellations with its names and bounding boxes from input files
#   The user can decide to write names on named stars or not
#   The window size is always 600 width by 600 height in pixels
#   Print all named stars with its values back to the console
#   Print the names of the stars in the constellation with its values onto the console
#   Output the xmin,xmax,ymin,ymax into a file
def main():
    #Handle the command line argument
    starFile,nameCheck=argHandler()
    #Read the star location file
    starTuplesList,starInfoFull,starInfoRemoved=readStarInfo(starFile)
    #set up window
    pointer = setup()
    #draw x and y axis
    drawAxes(pointer)
    #draw stars
    drawStars(pointer,starTuplesList,starInfoRemoved,nameCheck)
    #get the constellation file name from the user
    constell=input("Please enter a constellation filename\n>>")
    #check if it is valid, if not prompts for another (the user can also exit at this stage by pressing enter)
        
    counter=0
    #Loop until the user want to exit by hitting enter
    while constell!="":
        if not os.path.isfile(constell) and constell!="" :
            print("Invalid constellation filename\n")
            constell=input("Please enter a constellation filename\n>>")
        #read the constellation file
        starNamesList,constellName=readConstellInfo(constell)
        #get the appropriate color
        pointer.color(getColor(counter))
        #draw the constellation
        edgesXCoorList,edgesYCoorList=drawConstellation(pointer,starNamesList,starInfoFull)
        #draw the bounding box
        drawBoundBox(pointer,edgesXCoorList,edgesYCoorList,constellName)
        constell=input("Please enter a constellation filename\n>>")
        counter+=1
        
#Run the program
main()
