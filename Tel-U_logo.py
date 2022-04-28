import turtle

red1 = "#ec1c26"
red2 = "#b7242a"
gray1 = "#65666a"
gray2 = "#949496"

# Initializing the module
t = turtle.Turtle()
t.speed(8)
turtle.bgcolor('white')
t.color('white')
turtle.title("Tel-U logo")

######################
t.up()
t.goto(0, 150)
t.color(red1)
t.fillcolor(red1)
t.down()
t.begin_fill()
aim = 90
t.setheading(aim)
t.forward(100)
aim = 140
while (aim < 180):
    t.setheading(aim)
    t.forward(5)
    aim += 2
t.forward(29)
while (aim > 170):
    t.setheading(aim)
    t.forward(6)
    aim -= 1
aim = -90
t.setheading(aim)
t.forward(100)
aim = -10
while (aim < 0):
    t.setheading(aim)
    t.forward(6)
    aim += 1
t.forward(29)
while (aim > -40):
    t.setheading(aim)
    t.forward(5)
    aim -= 2
t.end_fill()
t.up()

######################
t.goto(0, 150)
t.color(red2)
t.fillcolor(red2)
t.down()
t.begin_fill()
aim = 90
t.setheading(aim)
t.forward(100)
aim = 40
while (aim > 0):
    t.setheading(aim)
    t.forward(5)
    aim -= 2
t.forward(29)
while (aim < 10):
    t.setheading(aim)
    t.forward(6)
    aim += 1
aim = -90
t.setheading(aim)
t.forward(100)
aim = 190
while (aim > 180):
    t.setheading(aim)
    t.forward(6)
    aim -= 1
t.forward(29)
while (aim < 220):
    t.setheading(aim)
    t.forward(5)
    aim += 2
t.end_fill()
t.up()

######################
#180
t.hideturtle()
t.goto(0, -110)
t.color(gray2)
t.setheading(0)
t.showturtle()
t.down()
t.fillcolor(gray2)
t.begin_fill()
t.circle(60, 90)
t.forward(120)
t.circle(-20, 90)
t.forward(100)
t.setheading(-90)
t.forward(140)
t.circle(-180, 180)
t.forward(140)
t.setheading(0)
t.forward(100)
t.circle(-20, 90)
t.forward(120)
t.circle(60, 90)
t.end_fill()

######################
t.color(gray1)
t.fillcolor(gray1)
t.begin_fill()
t.circle(60, 90)
t.setheading(-90)
t.forward(170)
aim = 19.5
t.setheading(180+aim)
t.circle(-180, aim*2)
t.setheading(90)
t.forward(170)
t.setheading(-90)
t.circle(60, 90)
t.end_fill()

t.hideturtle()
turtle.exitonclick()