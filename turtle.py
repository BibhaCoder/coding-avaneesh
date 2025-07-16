import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()
    


tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(1.5)
turtle.speed(10)
tommy.penup()
tommy.backward(100)
turtle.penup()
turtle.backward(100)
tommy.right(90)
tommy.forward(100)
tommy.right(-90)




for i in range(15):
  turtle.forward(10)
for i in range(20):
  tommy.forward(13)
turtle.forward(135)
tommy.forward(40)


