import turtle as tu
from pygame import mixer
mixer.init()

tu.Screen().bgcolor("black")
t=tu.Turtle()
t.pencolor("#de4e4b")
t.fillcolor("#de4e4b")
mixer.music.load("C:\Python311\Python\ganeshaaa.mp3")
mixer.music.play()
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Trunk
go(-130,150)

t.seth(-120)

t.begin_fill()
t.circle(100,90)
t.circle(280,10)
t.circle(-120,90)
t.circle(-60,150)
t.circle(-30,60)

t.seth(-120)
t.circle(30,60)
t.circle(55,150)
t.circle(120,77)
t.circle(-100,115)
t.end_fill()

go(0,50)
t.seth(20)
t.begin_fill()
t.circle(-50,80)
t.circle(-200,70)
t.circle(-50,60)


t.seth(-20)
t.circle(50,70)
t.circle(205,70)
t.circle(50,85)
t.end_fill()


go(70,10)
t.begin_fill()
t.seth(15)
t.circle(90,50)
t.end_fill()



#eyes
def eye():
    t.seth(-50)
    t.begin_fill()
    t.circle(20,120)
    t.seth(-90)
    t.circle(-17,165)
    t.end_fill()
go(-100,110)
eye()

go(40,110)
eye()

#Tilak
def cir(r):
    t.begin_fill()
    t.circle(r)
    t.end_fill()
go(0,150)
cir(10)

go(-1,125)
cir(8)

go(-4,105)
cir(5)

#crown
go(-80,200)
t.seth(30)
t.begin_fill()
t.circle(-150,60)
t.seth(141)
t.circle(120,80)
t.end_fill()

go(-70,225)
t.seth(30)
t.begin_fill()
t.circle(-120,60)
t.seth(141)
t.circle(95,80)
t.end_fill()

go(-30,280)
t.seth(-120)
t.begin_fill()
t.circle(20,250)
t.circle(-50,40)
t.seth(-100)
t.circle(50,42)
t.circle(-15,240)
t.end_fill()

go(-5,268)
cir(9)

#left year
go(-160,130)
t.seth(120)
t.begin_fill()
t.circle(70,60)
t.circle(15,100)
t.circle(90,30)
t.circle(-15,40)
t.circle(90,30)
t.circle(20,100)

t.seth(-130)
t.circle(-20,100)
t.circle(-90,30)
t.circle(15,35)
t.circle(-90,50)
t.circle(-18,80)
t.circle(-70,80)
t.end_fill()


#Right year
go(140,130)
t.seth(60)
t.begin_fill()
t.circle(-70,60)
t.circle(-15,100)
t.circle(-90,30)
t.circle(15,40)
t.circle(-90,30)
t.circle(-20,100)

t.seth(-50)
t.circle(20,100)
t.circle(90,30)
t.circle(-15,35)
t.circle(90,50)
t.circle(18,80)
t.circle(70,80)
t.end_fill()

mixer.music.play()
#Belly
go(-130,-20)
t.seth(-60)
t.begin_fill()
t.circle(-20,60)
t.circle(150,50)
t.circle(60,60)
t.seth(175)
t.circle(-70,70)
t.circle(-132,50)
t.circle(40,40)
t.end_fill()

#left leg
go(-90,-250)
t.seth(180)
t.begin_fill()
t.circle(-100,60)
t.circle(20,90)
t.circle(40,40)
t.circle(20,60)
t.circle(120,40)

t.seth(178)

t.circle(-120,40)
t.circle(-25,60)
t.circle(-50,50)
t.circle(-30,90)
t.circle(70,50)
t.end_fill()


#Right leg
go(120,-260)
t.seth(15)
t.begin_fill()
t.circle(120,50)
t.circle(20,90)
t.circle(70,40)
t.circle(120,40)
t.circle(-60,60)
t.circle(70,60)
t.circle(20,90)
t.seth(-120)
t.circle(20,120)
t.circle(40,50)
t.circle(-70,40)


t.seth(180)

t.circle(65,40)
t.circle(-35,40)
t.circle(-17,120)
t.seth(120)
t.circle(-14,70)
t.circle(-65,60)
t.circle(40,70)
t.circle(-115,50)
t.circle(-60,20)
t.circle(-15,98)
t.circle(-110,50)
t.end_fill()

#left hand
go(-170,-60)
t.seth(180)
t.begin_fill()
t.circle(20,80)
t.circle(-30,150)
t.circle(20,80)
t.seth(0)
t.circle(-20,80)
t.circle(32,170)
t.circle(-20,80)
t.end_fill()

go(-205,-80)
t.seth(75)
t.begin_fill()
t.circle(40,60)
t.seth(-150)
t.circle(40,60)
t.seth(65)
t.circle(-40,40)
t.seth(-45)
t.circle(-40,35)
t.end_fill()


#Right hand
go(240,-60)
t.seth(180)
t.begin_fill()
t.circle(20,80)
t.circle(-30,150)
t.circle(20,80)
t.seth(0)
t.circle(-20,80)
t.circle(32,170)
t.circle(-20,80)
t.end_fill()

go(205,-80)
t.seth(75)
t.begin_fill()
t.circle(40,60)
t.seth(-150)
t.circle(40,60)
t.seth(65)
t.circle(-40,40)
t.seth(-45)
t.circle(-40,35)
t.end_fill()


t.pencolor("orange")
go(450,200)
t.write("गणपती",align="center" ,font=("Arial",40,"bold"))
go(450,130)
t.write("बाप्पा ",align="center" ,font=("Arial",40,"bold"))
go(450,60)
t.write(" मोरया!",align="center" ,font=("Arial",40,"bold"))




t.hideturtle()
tu.done()





