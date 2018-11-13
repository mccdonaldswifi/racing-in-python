# This program allows the user to control two turtles with the keyboard.

from turtle import *

# These two variables create 2 turtle copies
turtle_1 = Turtle()
turtle_2 = Turtle()
#x = float(input("put in a value to represent the speed of the turtles: "))

#color1 = input("type a color for team 1: ")
#color2 = input("type a color for team 2: ")
#speed = input("type a number for how big the turtle steps are: ")


              
speed1 = 1
speed2 = 1

              
# These two lines of code define the color of each of the turtles
turtle_1.color("blue")
turtle_2.color("grey")



turtle_1.shape("turtle")
turtle_2.shape("turtle")



def turn_left_1():
    turtle_1.lt(30)


def turn_right_1():
    turtle_1.rt(30)

def turn_right_2():
    turtle_2.rt(30)

def turn_left_2():
    turtle_2.lt(30)




def increasespeed1():
    global speed1
    speed1 += 1




def decreasespeed1():
    global speed1
    speed1 -= 1

def increasespeed2():
    global speed2
    speed2 += 1

def decreasespeed2():
    global speed2
    speed2 -= 1

def up():
    turtle_1.pu

def down():
    turtle_1.pd

bgcolor("orange")
pu()
goto(-250, -150)
pd()
lt(90)
bk(50)
fd(50)
fd(300)
rt(90)
fd(150)
rt(90)
fd(300)
lt(90)
fd(150)
lt(90)
fd(250)
circle(-50, 180)


pu()
goto(-175, -150)
rt(180)
pd()
fd(250)
rt(180)
fd(300)
lt(90)
fd(275)
lt(90)
fd(300)
bk(300)
rt(90)
fd(50)
lt(90)
pu()
fd(50)
pd()
fd(250)
bk(250)
pu()
bk(50)
pd()
rt(90)
fd(75)
lt(90)
fd(50)
circle(25,90)
rt(90)
fd(225)
lt(90)




for i in range(14):
    fd(1)
    pu()
    fd(3)
    pd()

pu()

goto(300, 275)

pd()

fd(600)
lt(90)
fd(600)
lt(90)
fd(600)
lt(90)
fd(600)
lt(90)


color("orange")

#goto(0, 100)
type("draw a smiley face as fast as you can")
type(" space is pen up and b is pen down for both teams")

def pumpkin():
    turtle_1.goto(-200, -200)
    speed1 = 1

def apple():
    turtle_2.goto(-230, -200)
    speed2 = 1
    
    
listen()

# The functions below tell the computer which functions to execute when certain buttons are pressed
onkey(increasespeed1, "Up")
onkey(turn_right_1, "Right")
onkey(turn_left_1, "Left")
onkey(decreasespeed1, "Down")
onkey(increasespeed2, "w")
onkey(turn_right_2, "d")
onkey(turn_left_2, "a")
onkey(decreasespeed2, "s")
onkey(down, "space")
onkey(up, "b")
onkey(pumpkin, "j")
onkey(apple, "f")

#turtle_1.pu()
#turtle_2.pu()

while True:
    turtle_1.forward(speed1)
    turtle_2.forward(speed2)

    if turtle_1.xcor()> 300 or turtle_1.xcor() < -300:
        turtle_1.rt(180)
        

    if turtle_2.xcor()> 300 or turtle_2.xcor() < -300:
        turtle_2.rt(180)
       

    if turtle_1.ycor()> 275 or turtle_1.ycor() < -280:
        turtle_1.rt(180)
       

    if turtle_2.ycor()> 275 or turtle_2.ycor() < -300:
        turtle_2.rt(180)
        

   




exitonclick()
