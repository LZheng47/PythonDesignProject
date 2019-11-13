#TaintedFlower
#MainFile
from TaintedFlowerFunctions import*
turtle.tracer(0,0)
#fyi, the tracer(above) and update(at the end) commands completes program instantly.
#Remove tracer command to see process

background(66,87,245,66,245,147,1400)

origin()
MultiplePolygonSpiral(242,12,70,164,0,128,9,9,3)

origin()
for times in range(5):
    diamondspiral(64,227,216,64,77,227,50,70,times*72)

for times in range(5):
    diamondspiral(45,227,148,119,69,237,40,40,180+times*72)

for times in range(10):
    diamondspiral(127,66,201,82,47,222,10,20,18+times*36)

diamondspread("#4d59db",60,8,380)
diamondspread("#5d30d9",45,16,430)
diamondspread("#c92858",35,24,400)
diamondspread("#9e28c9",20,32,500)
diamondspread("#db4d7c",10,16,520)
diamondspread("#eb4444",15,8,540)

#Multiple color gradient background for Sigil
Tainted.penup()
SigilBackground(255,154,86,213,46,0,-380)
SigilBackground(255,186,173,255,154,86,-415)
SigilBackground(211,98,164,255,186,173,-450)
SigilBackground(165,1,98,211,98,164,-485)

Tainted.penup()
Tainted.goto(458,-378)
Tainted.setheading(0)
Tainted.pendown()
Tainted.width(5)
Tainted.pendown()

#Outline for gradient background
for times in range(2):
    for times in range(182):
        r1=110
        g1=52
        b1=235
        r2=52
        g2=64
        b2=235
        r=round(times*((r1-r2)/(181)))+r2
        g=round(times*((g1-g2)/(181)))+g2
        b=round(times*((b1-b2)/(181)))+b2
        c=(r,g,b)
        Tainted.color(c)
        Tainted.forward(1)
    Tainted.right(90)
    for times in range(142):
        r1=52
        g1=64
        b1=235
        r2=110
        g2=52
        b2=235
        r=round(times*((r1-r2)/(141)))+r2
        g=round(times*((g1-g2)/(141)))+g2
        b=round(times*((b1-b2)/(141)))+b2
        c=(r,g,b)
        Tainted.color(c)
        Tainted.forward(1)
    Tainted.right(90)

Tainted.setheading(0)
Tainted.penup()
Tainted.goto(550,-450)
Tainted.pendown()
Tainted.width(2)

doubletriangles("#1df035")
sidetriangles("#3de068")
Tainted.penup()
Tainted.forward(5)
Tainted.left(90)
Tainted.forward(5)
Tainted.right(90)
Tainted.pendown()
sidetriangles("#3de068")
Tainted.penup()
Tainted.forward(5)
Tainted.left(90)
Tainted.forward(5)
Tainted.left(90)


sidehexes("#3d03fc")
Tainted.penup()
Tainted.forward(35)
Tainted.left(90)
Tainted.forward(15)
Tainted.right(90)
Tainted.pendown()
sidehexes("#3d03fc")

Tainted.penup()
Tainted.forward(35)
Tainted.left(90)
Tainted.forward(15)
Tainted.right(90)
Tainted.pendown()

dash()
Tainted.penup()
Tainted.left(180)
Tainted.width(2)
Tainted.forward(5)
Tainted.right(90)
Tainted.forward(27)
Tainted.left(90)
Tainted.forward(27)
dash()
Tainted.penup()
Tainted.left(90)
Tainted.width(2)
Tainted.forward(10)
Tainted.right(90)
Tainted.forward(20)
Tainted.write("~RFX",False,align="left",font=("Comic Sans MS",11,"italic"))

turtle.update()
