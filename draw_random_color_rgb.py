from turtle import Turtle, Screen, colormode

square = Turtle()
import random
direction = [0, 90, 180, 270]
colour = ["red", "medium blue", "forest green", "lawn green", "yellow", "dodger blue", "medium spring green", "magenta"]
square.speed("fastest")

colormode(255)
def color_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    value = (r, g, b)
    return value

# def spriograph(size_of_gap):
      
#     for i in range(int(360 / size_of_gap)):
#         square.circle(100)
#         square.pencolor(color_random())
#         square.setheading(square.heading() + size_of_gap)

# spriograph(5)

for i in range(100):
    square.pensize(10)
    square.setheading(random.choice(direction))
    square.pencolor(color_random())
    square.forward(30)

screen_page = Screen()
screen_page.exitonclick()