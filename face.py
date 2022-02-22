#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle

#name our turtle "t"
t = turtle.Turtle()
sc = turtle.Screen()
#sc.mode('world')
t.getscreen()
sc.title("Little House on Prairie")
sc.setworldcoordinates(0, 0, 400, 400)
t.speed('fastest')
turtle.colormode(255)

#setting background color
sc.bgcolor(152,226,240)

#making the square hill 
t.penup()
t.goto(-10, 180)
t.pendown()
t.fillcolor(89,201,97)
t.begin_fill()
t.pencolor (89,201,97)
t.pensize(5)
t.setheading(0)
for side in range (4):
  t.forward(410)
  t.right(90)
t.end_fill()
t.penup()

#making the sun, a mixture of circles and triangles
t.goto(40,350)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.pencolor (245,190,38)
t.pensize(2)
t.setheading(90)
for repeats in range(20):
    t.forward(10)
    t.left(18)
    for sides in range(3):
        t.forward(50)
        t.right(120)
t.end_fill()
t.penup()

#making a house
t.goto(200,200)
t.pendown()
t.pencolor (245,190,38)
t.pensize(2)
t.fillcolor(247,218,173)
t.begin_fill()
t.setheading(180) #make turtle face left
for sides in range (3): #draw triangular part of roof
  t.forward (80)
  t.right(120)
for sides in range(2): #draw the rectangular entry face
  t.forward (80)
  t.left(90)
  t.forward(100)
  t.left(90)
t.setheading (25)
for sides in range (2):#draw parallelogram for the roof
  t.forward(130)
  t.left(95)
  t.forward(80)
  t.left(85)
for sides in range (2): #draw the retangular body of the house
  t.forward(130)
  t.right(115)
  t.forward(100)
  t.right(65)
t.penup()
t.end_fill()

#make a doorway
t.goto (140,100)
t.pendown()
t.setheading (90)
t.pencolor(193,57,37)
t.fillcolor(246,65,37)
t.begin_fill()
for side in range (2):
  t.forward (60)
  t.right(90)
  t.forward(40)
  t.right(90)
t.end_fill()
t.penup()

#make a doorhandle
t.goto (178,130)
t.pendown()
t.setheading (90)
t.pencolor(236,163,16)
t.fillcolor(249,182,48)
t.begin_fill()
t.circle(4)
t.end_fill()
t.penup()

#make roof window
t.goto (176,224)
t.pendown()
t.fillcolor(219,209,190)
t.pencolor(211,219,220)
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

#make a cross hatch for window
for n in range (4):
  t.goto(162,224)
  t.pendown()
  t.setheading(n*90)
  t.forward(8)
t.penup()

#make a window!
t.goto(215,185)
t.pendown()
t.begin_fill()
t.setheading (25)
for sides in range (2): 
  t.forward(100)
  t.right(115)
  t.forward(60)
  t.right(65)
t.end_fill()
t.penup()

turtle.done()

