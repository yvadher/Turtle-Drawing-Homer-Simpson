import turtle
def show():
    backGround()
    homer()

def backGround():
    
    turtle.seth(0)
    turtle.speed(10000)
    turtle.bgcolor("#1C32FA")
    turtle.penup()
    turtle.goto(130,-330)
    turtle.pendown()
    turtle.pen(pensize="10")
    turtle.color("#D8D8D8", "#67340A")
    turtle.begin_fill()
    turtle.circle(360,360)
    turtle.end_fill()
    turtle.penup()
    turtle.color("#D8D8D8","#0515A4")
    turtle.begin_fill()
    turtle.goto(130,-290)
    turtle.pendown()
    turtle.circle(320)
    turtle.end_fill()
    turtle.penup()
    
    turtle.goto(-600,300)
    turtle.pendown()
    turtle.color("#FAFAFA")
    turtle.pen(pencolor="#CECFD7",pensize="10")
    turtle.left(180)
    turtle.circle(35,35)
    turtle.circle(25,25)
    turtle.penup()
    turtle.goto(-600,300)
    turtle.pendown()
    turtle.left(120)
    turtle.forward(90)
    turtle.backward(75)
    turtle.right(90)
    turtle.forward(90)
    turtle.penup()
    turtle.goto(-525,210)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(28)
    turtle.penup()
    turtle.goto(-590,180)
    turtle.left(180)
    turtle.pendown()

    def curveright(frwrd, turn, angle, increment):
        counter4=0
        while(counter4<angle):
            turtle.right(turn)
            turtle.forward(frwrd)
            turn=turn+1
            counter4=counter4+increment

    def curveleft(frwrd, turn, angle, increment):
        counter4=0
        while(counter4<angle):
            turtle.left(turn)
            turtle.forward(frwrd)
            counter4=counter4+increment
            turn=turn+1
    turtle.right(8)
    curveleft(15,11,10,1)
    curveleft(6,8,7,1)
    turtle.goto(-590,180)
    turtle.goto(-590,90)
    turtle.right(120)
    curveleft(4,11,5,1)
    turtle.penup()
    turtle.goto(-555,180)
    turtle.pendown()
    turtle.seth(-90)
    turtle.forward(92)
    turtle.penup()
    turtle.goto(-500,150)
    turtle.pendown()
    turtle.right(93)
    turtle.circle(36,180)
    turtle.penup()
    turtle.goto(-450,150)
    turtle.pendown()
    turtle.left(180)
    turtle.circle(36)
    turtle.penup()
    turtle.goto(-395,180)
    turtle.left(93)
    turtle.pendown()
    turtle.forward(95)
    turtle.backward(45)
    turtle.left(180)
    turtle.circle(-20,180)
    turtle.forward(45)
    turtle.penup()
    turtle.goto(-300,150)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(36)
    turtle.penup()
    turtle.goto(-250,180)
    turtle.pendown()
    turtle.seth(-90)
    turtle.forward(95)
    turtle.end_fill()
    turtle.penup()
    turtle.pen(pensize="6")

    turtle.color("#FAFAF1","#FFFF26")
    turtle.goto(-600,0)
    turtle.seth(-90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(70)
    turtle.circle(25,180)
    turtle.seth(90)
    turtle.forward(70)
    turtle.backward(15)
    turtle.seth(0)
    turtle.end_fill()
    turtle.circle(-30,180)
    turtle.goto(-550,0)
    turtle.seth(180)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(-600,-10)
    turtle.seth(0)
    turtle.end_fill()
    turtle.pen(pensize="4")
    turtle.color("#E6E6E6","#E6E6E6")
    turtle.pendown()
    turtle.begin_fill()
    cur=0
    while cur<10:
        turtle.forward(5)
        turtle.right(3)
        cur=cur+1
    turtle.end_fill()


    
    turtle.color("#FAFAF1","#FFFF26")
    turtle.penup()
    turtle.goto(-500,0)
    turtle.seth(-90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(70)
    turtle.circle(25,180)
    turtle.seth(90)
    turtle.forward(70)
    turtle.backward(15)
    turtle.seth(0)
    turtle.end_fill()
    turtle.circle(-30,180)
    turtle.goto(-450,0)
    turtle.seth(180)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(-500,-10)
    turtle.seth(0)
    turtle.end_fill()
    turtle.pen(pensize="4")
    turtle.color("#E6E6E6","#E6E6E6")
    turtle.pendown()
    turtle.begin_fill()
    cur=0
    while cur<10:
        turtle.forward(5)
        turtle.right(3)
        cur=cur+1
    turtle.end_fill()


    
    turtle.color("#FAFAF1","#FFFF26")
    turtle.penup()
    turtle.goto(-395,0)
    turtle.seth(-90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(70)
    turtle.circle(25,180)
    turtle.seth(90)
    turtle.forward(70)
    turtle.backward(15)
    turtle.seth(0)
    turtle.end_fill()
    turtle.circle(-30,180)
    turtle.goto(-345,0)
    turtle.seth(180)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(-395,-10)
    turtle.seth(0)
    turtle.end_fill()
    turtle.pen(pensize="4")
    turtle.color("#E6E6E6","#E6E6E6")
    turtle.pendown()
    turtle.begin_fill()
    cur=0
    while cur<10:
        turtle.forward(5)
        turtle.right(3)
        cur=cur+1
    turtle.end_fill()






    turtle.seth(0)
    turtle.pensize()
    turtle.penup()
    turtle.goto(-650,-150)
    turtle.color("green")
    turtle.pendown()
    turtle.write("THE CAUSE OF-AND SOLUTION TO", True,align="left",font=("COMIC SANS MS", 22, "bold"))
    turtle.penup()
    turtle.goto(-600,-230)
    turtle.pendown()
    turtle.write("ALL LIFE PROBLEMS", True,align="left",font=("COMIC SANS MS", 22, "bold"))
    turtle.pensize()
   
 

    turtle.penup()
    turtle.color("#8A4B08","#DF0101")
    turtle.goto(-20,200)
    turtle.pendown()
    turtle.seth(0)
    turtle.begin_fill()
    turtle.circle(80)
    turtle.penup()
    turtle.goto(-20,115)
    turtle.pendown()
    turtle.circle(35)
    turtle.penup()
    turtle.goto(-20,60)
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()
    turtle.penup()
    turtle.color("#FBFBEF", "#FBFBEF")
   
    turtle.goto(-68,260)
    turtle.write("Umm..!!!",align="left",font=("arial",25,"normal"))
    turtle.goto(0,0)
    turtle.end_fill()
    turtle.pensize()
    turtle.penup()
    turtle.seth(0)
    turtle.goto(0,0)
    turtle.pendown()

    


def homer():
    turtle.pendown()
    turtle.speed(10000)
    lefteye()
    righteye()
    head()
    mouth()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    ear()
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.backward(25)
    turtle.pendown()
    hairone()
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(0,0)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(120)
    turtle.pendown()
    hairtwo()
    turtle.penup()
    turtle.left(90)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.pendown()
    hairtwo()
    
def righteye():
    turtle.left(90)
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.pen(pensize=5)
    counter=0
    while(counter<360):
        turtle.forward(1)
        turtle.right(1)
        counter=counter+1
    turtle.end_fill()
    turtle.penup()
    turtle.right(60)
    turtle.forward(50)
    turtle.pendown()
    turtle.color("black", "black")
    turtle.begin_fill()
    counter2=1
    while(counter2<=360):
        turtle.forward(3)
        turtle.right(20)
        counter2=counter2+18
    turtle.end_fill()
    turtle.penup()
    turtle.backward(50)
    turtle.setheading(0)
    

def lefteye():
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.pendown
    turtle.pen(pensize=5)
    counter=1
    while(counter<=360):
        turtle.forward(1)
        turtle.right(1)
        counter=counter+1
    turtle.end_fill()
    turtle.penup()
    while(counter>=300):
        turtle.backward(1)
        turtle.left(1)
        counter=counter-1
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.color("black", "black")
    turtle.begin_fill()
    counter2=1
    while(counter2<=360):
        turtle.forward(3)
        turtle.right(20)
        counter2=counter2+18
    turtle.end_fill()
    turtle.penup()
    turtle.backward(20)
    turtle.left(90)
    while(counter>=270):
        turtle.backward(1)
        turtle.left(1)
        counter=counter-1
    turtle.setheading(0)
    turtle.right(10)
    turtle.forward(110)
    turtle.setheading(0)

def curveright(frwrd, turn, angle, increment):
    counter4=0
    while(counter4<angle):
        turtle.right(turn)
        turtle.forward(frwrd)
        counter4=counter4+increment

def curveleft(frwrd, turn, angle, increment):
    counter4=0
    while(counter4<angle):
        turtle.left(turn)
        turtle.forward(frwrd)
        counter4=counter4+increment

def head():
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.pendown()
    turtle.color("black", "#FFD90F")
    turtle.begin_fill()
    turtle.forward(60)
    counter3=1
    while(counter3<=180):
        turtle.left(2)
        turtle.forward(1)
        counter3=counter3+2
    counter3=0
    while(counter3<=10):
        turtle.forward(3)
        turtle.left(1)
        counter3=counter3+1
    turtle.forward(20)
    counter3=0
    while(counter3<=90):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+1
    turtle.forward(20)
    counter3=0
    while(counter3<=90):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+1
    turtle.forward(5)
    counter3=0
    while(counter3<=75):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+1
        counter3=counter3+1
    turtle.forward(30)
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(30)
    curveright(1, 2, 30, 1)
    turtle.setheading(0)
    turtle.forward(225)
    turtle.left(110)
    curveright(6, 1, 30, 1)

    turtle.forward(200)
    curveleft(2, 1, 180, 1)
    turtle.forward(105)
    curveright(1, 2, 10, 1)
    turtle.left(135)
    curveright(1, 1, 83, 1)
    turtle.left(135)
    curveright(1, 1, 310, 1)
    turtle.end_fill()

def mouth():
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(145)
    turtle.left(90)
    turtle.pendown()
    turtle.color("black", "#D1B270")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(37)
    counter3=0
    while(counter3<=90):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+1
    turtle.forward(20)
    counter3=0
    while(counter3<=90):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+1
    turtle.forward(5)
    counter3=0
    while(counter3<=90):
        turtle.right(1)
        turtle.forward(1)
        counter3=counter3+2
    turtle.right(10)
    turtle.forward(75)
    curveright(1, 5, 40, 1)
    counter3=0
    while(counter3<10):
        turtle.left(5)
        turtle.backward(1)
        counter3=counter3+1
    turtle.left(60)
    curveleft(2, 0.5, 20, 0.5)
    turtle.end_fill()

def ear():
    turtle.color("black", "#FFD90F")
    turtle.begin_fill()
    curveleft(0.5, 1, 180, 1)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    curveright(0.25, 1, 180, 1)
    turtle.end_fill()

def hairone():
    turtle.left(90)
    turtle.right(30)
    turtle.forward(60)
    turtle.left(30)
    turtle.backward(55)
    turtle.right(60)
    turtle.forward(50)
    turtle.left(30)
    turtle.backward(60)

def hairtwo():
    turtle.left(90)
    curveright(1, 1, 180, 1)
    turtle.forward(10)

    




