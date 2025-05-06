import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('Purple')
t = turtle.Turtle()
#intro screen
t.penup()
t.goto(0,295)
t.pendown()
t.write("Intro", font=("arial", 30, "normal"), align="center")




t.penup()
t.goto(0,200)
t.pendown()
t.write("All About", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(-150,0)
t.pendown()
screen.addshape("m1.gif")
t.shape("m1.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150,0)
t.pendown()
screen.addshape("m3.gif")
t.shape("m3.gif")
t.stamp()
t.shape("classic")

#circle
t.penup()
t.goto(0,0)
t.fillcolor('pink')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(0,-195)
t.pendown()
t.write("Me!", font=("arial", 30, "bold"), align="center")


t.penup()
t.goto(0,-295)
t.pendown()
t.write("Brisa Subedi", font=("arial", 17, "bold"), align="center")



t.penup()
t.goto(180,300)
t.pendown()
t.write("Press Enter to Continue", font=("arial", 15, "bold"), align="center")

round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('Blue')
t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite Foods", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(100,150)
t.pendown()
t.write("Pizza", font=("arial", 30, "bold"), align="center")
t.penup()

t.goto(-100,150)
t.pendown()
screen.addshape("pizza2.gif")
t.shape("pizza2.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(100,-20)
t.pendown()
t.write("Ice Cream", font=("arial", 30, "bold"), align="center")
t.penup()

t.goto(-100,-30)
t.pendown()
screen.addshape("icecream.gif")
t.shape("icecream.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(100,-250)
t.pendown()
t.write("Mozzarella Sticks", font=("arial", 20, "bold"), align="center")
t.penup()

t.goto(-100,-250)
t.pendown()
screen.addshape("m.gif")
t.shape("m.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-180,300)
t.pendown()
t.pencolor('black')
t.fillcolor('green')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.end_fill()

t.penup()
t.goto(180,300)
t.pendown()
t.write("Press Enter to Continue", font=("arial", 15, "bold"), align="center")

round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('Yellow')
t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite Hobbies", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(-200,150)
t.pendown()
screen.addshape("c.gif")
t.shape("c.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,150)
t.pendown()
t.write("Crochet", font=("arial", 30, "bold"), align="center")
t.penup()

t.penup()
t.goto(0,0)
t.pendown()
t.write("Being with my cat", font=("arial", 15, "bold"), align="center")


t.penup()
t.goto(-200,0)
t.pendown()
screen.addshape("y.gif")
t.shape("y.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-50,-150)
t.pendown()
t.write("Singing", font=("arial", 20, "bold"), align="center")
t.penup()

t.goto(-200,-150)
t.pendown()
screen.addshape("c2.gif")
t.shape("c2.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-50,-300)
t.pendown()
t.write("Ceramics", font=("arial", 20, "bold"), align="center")
t.penup()

t.goto(-200,-300)
t.pendown()
screen.addshape("c4.gif")
t.shape("c4.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150,0)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.goto(150,0)
t.goto(250,0)
t.goto(200,100)
t.goto(150,0)
t.end_fill()

t.penup()
t.goto(180,300)
t.pendown()
t.write("Press Enter to Continue", font=("arial", 15, "bold"), align="center")

round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('Red')
t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite Movie", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(95,100)
t.pendown()
screen.addshape("c2o.gif")
t.shape("c2o.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-95,100)
t.pendown()
screen.addshape("co2.gif")
t.shape("co2.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,-125)
t.pendown()
t.write("Coraline is my favorite movie. ", font=("arial", 20, "bold"), align="center")
t.penup()


t.penup()
t.goto(0,-150)
t.pendown()
t.write("I used to always watch it as a kid and  ", font=("arial", 20, "bold"), align="center")
t.penup()

t.penup()
t.goto(0,-175)
t.pendown()
t.write("I love the vibes that the movie gives off. ", font=("arial", 20, "bold"), align="center")
t.penup()

t.penup()
t.goto(0,-200)
t.pendown()
t.write("The suspense in the movie is fantastic and the  ", font=("arial", 20, "bold"), align="center")
t.penup()

t.penup()
t.goto(0,-225)
t.pendown()
t.write("animation is fascinating. ", font=("arial", 20, "bold"), align="center")
t.penup()

#square
t.goto(-300,260)

t.penup()
t.fillcolor("brown")
t.begin_fill()
t.setheading(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()



t.penup()
t.goto(180,300)
t.pendown()
t.write("Press Enter to Continue", font=("arial", 15, "bold"), align="center")
round = input("Press Enter to Continue: ")


t.clear()
screen.bgcolor('orange')
t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite Sport", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(0,-45)
t.pendown()
t.write("Track and Field", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(-95,150)
t.pendown()
screen.addshape("trr.gif")
t.shape("trr.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(95,150)
t.pendown()
screen.addshape("t44.gif")
t.shape("t44.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(0,-135)
t.pendown()
t.write("Track and Field is my favorite sport,", font=("arial", 20, "bold"), align="center")

t.penup()
t.goto(0,-159)
t.pendown()
t.write("because I run it. I love the variety of", font=("arial", 20, "bold"), align="center")

t.penup()
t.goto(0,-189)
t.pendown()
t.write("events you can do, such as running,", font=("arial", 20, "bold"), align="center")


t.penup()
t.goto(0,-219)
t.pendown()
t.write("jumping, throwing, etc. Since track is an ", font=("arial", 20, "bold"), align="center")



t.penup()
t.goto(0,-249)
t.pendown()
t.write("independent sport, all the hard work you do", font=("arial", 20, "bold"), align="center")


t.penup()
t.goto(0,-279)
t.pendown()
t.write("goes to yourself.", font=("arial", 20, "bold"), align="center")
t.penup()
#square
t.goto(250,250)
t.penup()
t.fillcolor('cyan')
t.begin_fill()
t.setheading(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


t.penup()
t.goto(-245,279)
t.pendown()
t.write("The End!", font=("arial", 20, "bold"), align="center")












turtle.done()