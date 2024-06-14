import turtle

kali = turtle

def w():
    kali.forward(10)

def s():
    kali.backward(10)

def left():
    new_line = kali.heading() + 10
    kali.setheading(new_line)

def right():
    new_line = kali.heading() - 10
    kali.setheading(new_line)

def clear():
    kali.clear()
    kali.penup()
    kali.home()
    kali.pendown()

kali.listen()
kali.onkey(fun=w , key="w" )
kali.onkey(fun=s, key="s")
kali.onkey(fun=left, key="a")
kali.onkey(fun=right, key="d" )
kali.onkey(fun=clear, key="c")
screen = turtle.Screen()
screen.exitonclick()

