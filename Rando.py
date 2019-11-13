import turtle
Tainted=turtle.Turtle()
turtle.colormode(255)
turtle.tracer(0,0)
Tainted.width(3)
Tainted.speed(0)
turtle.bgcolor("black")

def ws(c,d,s):
    Tainted.color(c)
    for times in range(s):
        Tainted.forward(d)
        Tainted.left(360/s)
def wss(c,d,s,a,do):
    for times in range(a):            
        Tainted.penup()
        Tainted.home()
        Tainted.left(360/a*times)
        Tainted.forward(do)
        Tainted.pendown()
        ws(c,d,s)
wss("#d6495e",100,5,20,0)
wss("#5b76cf",50,5,15,0)
wss("#4baddb",50,5,10,40)
wss("#675bcf",20,5,6,100)
wss("#8b5bcf",30,7,9,200)
wss("#5bcfa2",20,3,15,270)
turtle.update()
