import turtle

# Initializing the module
t = turtle.Turtle()
t.speed(4)
turtle.bgcolor('white')
t.color('white')
turtle.title("Netflix logo")

# Drawing the black background
t.up()
t.goto(-100, 160)
t.down()
t.color("black")
t.fillcolor("black")
t.begin_fill()

t.forward(200)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(200)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(30)
t.end_fill()

# Drawing the N shape
t.up()
t.color("black")
t.setheading(270)
t.forward(240)
t.setheading(0)
t.forward(10)

t.down()
t.color("#a10808")
t.fillcolor("#a10808")
t.begin_fill()
t.setheading(5)
t.forward(35)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(35)
t.setheading(270)
t.forward(180)
t.end_fill()
t.setheading(0)

t.up()
t.forward(75)
t.down()
t.color("#a10808")
t.fillcolor("#a10808")
t.begin_fill()
t.setheading(-5)
t.forward(35)
t.setheading(90)
t.forward(183)
t.setheading(180)
t.forward(35)
t.setheading(270)
t.forward(180)
t.end_fill()

t.color("#e60909")
t.fillcolor("#e60909")
t.begin_fill()
t.setheading(113)
t.forward(195)
t.setheading(0)
t.forward(36)
t.setheading(293)
t.forward(199)
t.end_fill()
t.hideturtle()

turtle.exitonclick()