#CPSC231 LEC01 TUT02
#NAME: Daniel Nguyen
#ID: 30102065
#DATE: September 27th 2019
#Description: this program creates a window with x and y axis, asks inputs from the user to draw a circle and line(s), and then calculates and circles the intersection(s)

#imports necessary libraries
import turtle
import math

#sets constants and variables
WIDTH = 800
HEIGHT = 600
RADIUS = 5
loop = True
count=0

#draws the axis, the lines, the circles, or the "No Intersections" message according to the case
def draw(num1,num2,num3,num4,case):
    pointer = turtle.Turtle()
    pointer.hideturtle()
    pointer.penup()
    pointer.goto(num1,num2)
    pointer.pendown()
    #customize the pen size and speed
    pointer.speed("fastest")
    pointer.pensize(3)
    #case 0 is to draw the axis
    if case==0:
        pointer.goto(num3,num4)
    #case 1 is to draw the line
    elif case==1:
        pointer.color("blue")
        pointer.goto(num3,num4)
    #case 2 is to draw the circle
    elif case==2:
        pointer.color("red")
        pointer.circle(num3)
    else:
        pointer.color("green")
        #case 3 is to give the "No Intersections" message
        if case==3:
            pointer.write("No intersections",align="center",font=("Arial", 20, "italic"))
        #circles the intersection(s)
        else:
            pointer.circle(RADIUS)
            
#Sets up the window and the axis         
screen = turtle.getscreen()
screen.setup(WIDTH,HEIGHT,0,0)
screen.setworldcoordinates(0,0,WIDTH,HEIGHT)       
draw(0,HEIGHT/2,WIDTH,HEIGHT/2,0)
draw(WIDTH/2,0,WIDTH/2,HEIGHT,0)

#gets input from the user to draw the circle
xc=int(input("Please enter the x value of the center of the circle\n>"))
yc=int(input("Please enter the y value of the center of the circle\n>"))
r=float(input("Please enter the radius of the circle\n>"))
draw(xc,yc-r,r,0,2)

#loops to draw more lines and get its intersections with the circle until the user wants to exit
while loop:
    try:
        #gets inputs from the user to draw a line
        x1=int(input("Please enter the x value of the starting point of the line\n>"))
        y1=int(input("Please enter the y value of the starting point of the line\n>"))
        x2=int(input("Please enter the x value of the ending point of the line\n>"))
        y2=int(input("Please enter the y value of the ending point of the line\n>"))
        draw(x1,y1,x2,y2,1)
        
        #calculates the discriminant
        a=(x2-x1)**2 +(y2-y1)**2
        b=2*((x1-xc)*(x2-x1)+(y1-yc)*(y2-y1))
        c=(x1-xc)**2+(y1-yc)**2-r**2
        delta=b**2-4*a*c
        #determines the intersections if they exist and circles it. If they don't, draw "No intersections"
        if delta<0:
            draw(WIDTH/2,HEIGHT/2,0,0,3)
        elif delta==0:
            alp= -b/(2*a)
            if 0<=alp<=1:
                x_int=(1-alp)*x1+alp*x2
                y_int=(1-alp)*y1+alp*y2
                draw(x_int,y_int-RADIUS,0,0,4)
                count+=1
            else:
                draw(WIDTH/2,HEIGHT/2,0,0,3)
        else:
            alp1=(-b+math.sqrt(delta))/(2*a)
            alp2=(-b-math.sqrt(delta))/(2*a)
            if 0<=alp1<=1:
                x_int1=(1-alp1)*x1+alp1*x2
                y_int1=(1-alp1)*y1+alp1*y2
                draw(x_int1,y_int1-RADIUS,0,0,4)
                count+=1
            if 0<=alp2<=1:
                x_int2=(1-alp2)*x1+alp2*x2
                y_int2=(1-alp2)*y1+alp2*y2
                draw(x_int2,y_int2-RADIUS,0,0,4)
                count+=1
            if (alp1>1 or alp1<0) and (alp2>1 or alp2<0):
                draw(WIDTH/2,HEIGHT/2,0,0,3)
        print("\n\n***YOU HAVE FOUND ",count," INTERSECTION(S) SO FAR***\n\n")
    #when the user pass an empty input, this will be executed to exit the loop 
    except ValueError:
        print("\n\nTHANK YOU FOR USING THIS APPLICATION\n\n")
        loop=False
exit()









