#RegretfulHorizon FunctionFile
import turtle
from random import seed
from random import randint
from random import choice
Tainted=turtle.Turtle()
Tainted.speed(0)
turtle.colormode(255)

def bgcolor(r1,g1,b1,r2,g2,b2,x,y,d,i):
    for times in range(i):
        r=round(times*((r1-r2)/(i-1)))+r2
        g=round(times*((g1-g2)/(i-1)))+g2
        b=round(times*((b1-b2)/(i-1)))+b2
        c=(r,g,b)
        Tainted.color(c)
        Tainted.penup()
        Tainted.goto(x,y)
        Tainted.setheading(270)
        Tainted.forward((i*2)-times*2)
        Tainted.setheading(0)
        Tainted.begin_fill()
        Tainted.circle((i*2)-(times*2)+d)
        Tainted.end_fill()

def star1(x,y,c,d,a):
    Tainted.penup()
    Tainted.goto(x,y)
    Tainted.color(c)
    Tainted.left(a)
    Tainted.pendown()
    Tainted.begin_fill()
    for times in range(5):
        Tainted.forward(d)
        Tainted.right(144)
    Tainted.end_fill()

#Sin(30) = 0.5 | Hypothenus(H) is d/sin(30)
def star2(x,y,c,d):
    H=d/0.5
    Tainted.penup()
    Tainted.goto(x,y)
    Tainted.color(c)
    Tainted.pendown()
    Tainted.begin_fill()
    Tainted.setheading(90)
    Tainted.right(30)
    Tainted.forward(H) 
    Tainted.left(60)
    Tainted.forward(H)
    Tainted.left(120)
    Tainted.forward(H)
    Tainted.left(60)
    Tainted.forward(H)
    Tainted.end_fill()

def seagt(y):
    Tainted.penup()
    Tainted.goto(-700,y)
    Tainted.pendown()
    Tainted.setheading(0)
#1 is lighter color
#2 is darkest color
#3 is lightest color
def sea(r1,g1,b1,r2,g2,b2,r3,g3,b3):
    Tainted.width(5)
    for times in range(105):
        seagt(0-times*5)
        i1=500+(round(times/2.5))
        i2=200-(round(times/2.5))
        for times in range(i1):
            r=round(times*((r1-r2)/(i1-1)))+r2
            g=round(times*((g1-g2)/(i1-1)))+g2
            b=round(times*((b1-b2)/(i1-1)))+b2
            c=(r,g,b)
            Tainted.color(c)
            Tainted.forward(1)
        for times in range(i2):
            r=round(times*((r3-r1)/(i2-1)))+r1
            g=round(times*((g3-g1)/(i2-1)))+g1
            b=round(times*((b3-b1)/(i2-1)))+b1
            c=(r,g,b)
            Tainted.color(c)
            Tainted.forward(1)
        for times in range(i2):
            r=round(times*((r1-r3)/(i2-1)))+r3
            g=round(times*((g1-g3)/(i2-1)))+g3
            b=round(times*((b1-b3)/(i2-1)))+b3
            c=(r,g,b)
            Tainted.color(c)
            Tainted.forward(1)
        for times in range(i1):
            r=round(times*((r2-r1)/(i1-1)))+r1
            g=round(times*((g2-g1)/(i1-1)))+g1
            b=round(times*((b2-b1)/(i1-1)))+b1
            c=(r,g,b)
            Tainted.color(c)
            Tainted.forward(1)
