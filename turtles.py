import turtle
turtle.Screen().bgcolor("lightgreen")
t=turtle.Screen()
t.setup(400,300)

t.title("Let's create drawings: How to draw a Square")
t=turtle.Turtle()
t.shape("circle")
t.color("red")
t.pensize(5)

t.fillcolor("cyan")

t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

turtle.done()


