import turtle
sqd = turtle.Turtle()
for i in range(4):
    sqd.forward(70)
    sqd.left(90)
    
sqd.left(45)

for i in range(10):
    sqd.penup()
    sqd.forward(10)
    sqd.pendown()
    sqd.dot()
