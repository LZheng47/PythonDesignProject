#TaintedFlower
#FunctionFile
import turtle
turtle.screensize(1400,1400)
turtle.colormode(255)
Tainted=turtle.Turtle()
Tainted.speed(0)
Tainted.ht()

#i=iteratins
#r1,g1,b1 are hex values for first color
#r2,g2,b2 are hex values for second color
def background(r1,g1,b1,r2,g2,b2,i):
    Tainted.penup()
    Tainted.goto(-i/2,i/2)
    Tainted.pendown()
    Tainted.setheading(90)
    for times in range(i):
        r=round(times*((r1-r2)/(i-1)))+r2
        g=round(times*((g1-g2)/(i-1)))+g2
        b=round(times*((b1-b2)/(i-1)))+b2
        c=(r,g,b)
        Tainted.color(c)
        Tainted.goto(-i/2+times,i/2)
        Tainted.setheading(270)
        Tainted.forward(i)
        Tainted.pendown()

def origin():
    Tainted.penup()
    Tainted.home()
    Tainted.pendown()
#c=color
#d=distance
#s=sides for polygon
#n=number of polygons
def MultiplePolygons(c,d,s,n):
    angle=360/s
    Tainted.color(c)
    for times in range(n):
        Tainted.begin_fill()
        for times in range(s):
            Tainted.forward(d)
            Tainted.left(angle)
        Tainted.end_fill()
        Tainted.left(360/n)

#p=spiraldegree
def MultiplePolygonSpiral(r1,g1,b1,r2,g2,b2,s,n,p):
    i=127
    for times in range(i):
        r=round(times*((r1-r2)/(i-1)))+r2
        g=round(times*((g1-g2)/(i-1)))+g2
        b=round(times*((b1-b2)/(i-1)))+b2
        c=(r,g,b)
        d=(130-times)
        MultiplePolygons(c,d,s,n)
        Tainted.left(360/p-1)

#sin(10) is 0.1736481777
#sin(20) is 0.3420201433
#^Used to calculate hypotenuse distance with specific angles
def diamond(c,d):
    Tainted.color(c)
    Tainted.begin_fill()
    Tainted.left(10)
    Tainted.forward(d)
    Tainted.right(30)
    Tainted.forward(d*0.1736481777/0.3420201433)
    Tainted.right(140)
    Tainted.forward(d*0.1736481777/0.3420201433)
    Tainted.right(30)
    Tainted.forward(d)
    Tainted.end_fill()
    Tainted.right(170)

#a=angleofdiamonds
def diamondspiral(r1,g1,b1,r2,g2,b2,d,i,a):
    for times in range(i):
        r=round(times*((r1-r2)/(i-1)))+r2
        g=round(times*((g1-g2)/(i-1)))+g2
        b=round(times*((b1-b2)/(i-1)))+b2
        c=(r,g,b)
        origin()
        Tainted.left(90)
        Tainted.left(a)
        Tainted.penup()
        Tainted.forward(i-times*1.5)
        Tainted.pendown()
        Tainted.right((i*0.25)-(times/4))
        diamond(c,i-(times*1.5)+95)

#do=distance from origin
def diamondspread(c,d,i,do):
    for times in range(i):
        Tainted.color(c)
        origin()
        Tainted.penup()
        Tainted.left(times*360/i)
        Tainted.forward(do)
        Tainted.pendown()
        diamond(c,d)

#RFX Sigil - Signature 
def SigilBackground(r1,g1,b1,r2,g2,b2,x):
    for times in range(35):
        r=round(times*((r1-r2)/(34)))+r2
        g=round(times*((g1-g2)/(34)))+g2
        b=round(times*((b1-b2)/(34)))+b2
        c=(r,g,b)
        Tainted.color(c)
        Tainted.goto(460,x-times)
        Tainted.setheading(0)
        Tainted.forward(180)
        Tainted.pendown()

#Different Compenents used to complete Sigil
def doubletriangles(c):
        Tainted.pencolor("black")
        Tainted.fillcolor(c)
        Tainted.begin_fill()
        Tainted.forward(20)
        Tainted.right(110)
        Tainted.forward(58)
        Tainted.right(160)
        Tainted.forward(109)
        Tainted.left(160)
        Tainted.forward(58)
        Tainted.left(110)
        Tainted.forward(20)
        Tainted.end_fill()

def sidetriangles(c):
    Tainted.left(90)
    Tainted.penup()
    Tainted.forward(5)
    Tainted.right(90)
    Tainted.forward(5)
    Tainted.left(90)
    Tainted.pendown()
    Tainted.fillcolor(c)
    Tainted.begin_fill()
    Tainted.forward(49)
    Tainted.right(165)
    Tainted.forward(51)
    Tainted.right(105)
    Tainted.forward(13)
    Tainted.end_fill()

def sidehexes(c):
    Tainted.penup()
    Tainted.forward(27)
    Tainted.pendown()
    Tainted.fillcolor(c)
    Tainted.begin_fill()
    Tainted.forward(23)
    Tainted.left(105)
    Tainted.forward(7)
    Tainted.left(75)
    Tainted.forward(18)
    Tainted.right(75)
    Tainted.forward(56)
    Tainted.left(75)
    Tainted.forward(7)
    Tainted.left(105)
    Tainted.forward(63)
    Tainted.end_fill()
    Tainted.penup()
    Tainted.left(165)
    Tainted.forward(13)
    Tainted.right(90)
    Tainted.forward(10)
    Tainted.left(105)
    Tainted.pendown()
    Tainted.fillcolor("#18ede2")
    Tainted.begin_fill()
    Tainted.forward(40)
    Tainted.right(170)
    Tainted.forward(43)
    Tainted.right(115)
    Tainted.forward(7)
    Tainted.end_fill()

def dash():
    Tainted.penup()
    Tainted.forward(27)
    Tainted.right(90)
    Tainted.forward(27)
    Tainted.left(90)
    Tainted.pendown()
    Tainted.width(2.5)
    Tainted.forward(5)
