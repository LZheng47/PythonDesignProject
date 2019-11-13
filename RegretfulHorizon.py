#RegretfulHorizon MainFile
from RegretfulHorizonFunctions import*
#--MAY TAKE A WHILE TO LOAD--
turtle.screensize(1400,1000)
turtle.tracer(0,0)
Tainted.penup()
Tainted.goto(-450,250)
Tainted.pendown()

#background/sky
bgcolor(98,109,209,31,8,66,-450,250,50,850)
bgcolor(135,156,232,113,118,206,-450,250,50,15)

#random star dispersal
for times in range(100):
    sequence=["yellow"
              ,"#f7f5a8","#f2ef6d","#f5ffab","#fbffe0","#f9faeb","#f6fac3","#faf2b6"]
    x=randint(-700,700)
    y=randint(-500,500)
    c=choice(sequence)
    d=randint(3,7)
    a=randint(0,360)
    star1(x,y,c,d,a)
for times in range(100):
    sequence=["yellow","white"
              ,"#f7f5a8","#f2ef6d","#f5ffab","#fbffe0","#f9faeb","#f6fac3","#faf2b6"]
    x=randint(-700,700)
    y=randint(-500,500)
    c=choice(sequence)
    d=randint(1,2)
    star2(x,y,c,d)

#yellow moon
Tainted.penup()
Tainted.goto(-450,250)
Tainted.pendown()
i=50
for times in range(i):
    r1=236
    g1=237
    b1=216
    r2=240
    g2=238
    b2=189
    r=round(times*((r1-r2)/(i-1)))+r2
    g=round(times*((g1-g2)/(i-1)))+g2
    b=round(times*((b1-b2)/(i-1)))+b2
    c=(r,g,b)
    Tainted.color(c)
    Tainted.penup()
    Tainted.setheading(90)
    Tainted.forward(times/i)
    Tainted.setheading(0)
    Tainted.begin_fill()
    Tainted.circle(i-times)
    Tainted.end_fill()

#background "green" moon
bgcolor(101,158,168,82,78,166,0,-40,80,30)
Tainted.penup()
Tainted.goto(0,-40)
Tainted.pendown()

#center green "moon"
i=80
for times in range(i):
    r1=140
    g1=237
    b1=185
    r2=123
    g2=232
    b2=174
    r=round(times*((r1-r2)/(i-1)))+r2
    g=round(times*((g1-g2)/(i-1)))+g2
    b=round(times*((b1-b2)/(i-1)))+b2
    c=(r,g,b)
    Tainted.color(c)
    Tainted.penup()
    Tainted.setheading(90)
    Tainted.forward(times/i)
    Tainted.setheading(0)
    Tainted.begin_fill()
    Tainted.circle(i-times)
    Tainted.end_fill()

#sea
sea(68,118,199,26,37,112,103,219,151)

Tainted.width(1)
Tainted.color("white")

Tainted.penup()
Tainted.goto(-701,1000)
Tainted.pendown()
Tainted.setheading(180)
Tainted.begin_fill()
for times in range(2):
    Tainted.forward(1000)
    Tainted.left(90)
    Tainted.forward(3000)
    Tainted.left(90)
Tainted.end_fill()

Tainted.penup()
Tainted.goto(701,1000)
Tainted.pendown()
Tainted.setheading(0)
Tainted.begin_fill()
for times in range(2):
    Tainted.forward(1000)
    Tainted.right(90)
    Tainted.forward(3000)
    Tainted.right(90)
Tainted.end_fill()

Tainted.ht()
turtle.update()
