import turtle
a = turtle.Turtle()
a.fillcolor("yellow")
a.speed(10)
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.left(360/6)
a.end_fill()
a.fillcolor("red")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.right(360/6)
a.end_fill()
a.pu()
a.goto(74,43)
a.pd()
a.fillcolor("blue")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.right(360/6)
a.end_fill()
a.pu()
a.goto(-24,-43)
a.pd()
a.left(180)
a.fillcolor("orange")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.right(360/6)
a.end_fill()
a.fillcolor("black")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.left(360/6)
a.end_fill()
a.pu()
a.backward(148)
a.pd()
a.fillcolor("green")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.left(360/6)
a.end_fill()
a.pu()
a.forward(50)
a.left(60)
a.forward(50)
a.right(60)
a.forward(50)
a.left(60)
a.pd()
a.fillcolor("brown")
a.begin_fill()
for i in range(6):
    a.forward(50)
    a.left(360/6)
a.end_fill()






