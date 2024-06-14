from turtle import Turtle, Screen, colormode

square = Turtle()
square.color("green")
# square.forward(90)
# square.right(90)
# square.forward(90)
# square.right(90)
# square.forward(90)
# square.right(90)
# square.forward(90)

# for square1 in range(0, 4):
#     square.forward(100)
#     square.right(90)

# for i in range(10):
#     square.color("Black")
#     square.forward(20)
#     square.color("white")
#     square.forward(20)
    
# for _ in range(15):
#     square.forward(10)
#     square.penup()
#     square.forward(10)
#     square.pendown()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         square.color(c)
#         square.forward(steps)
#         square.right(30)


# for n in range (4):
#     for c in ("red", "blue", "green"):
#         square.color(c)
#         square.circle(50)
#         square.right(30)

# while True:
#     square.forward(200)
#     square.left(170)
#     if abs(square.pos()) < 1:
#         break

# import random
# color = ["red", "blue", "green"]
# for _ in range(10):
#     for i in range(4):
#         for c in("red", "blue", "green"):
#                 square.color(c)
#                 square.forward(40)
#                 square.left(72)
#                 square.forward(40)
#                 square.left(72)
# import random
# colour = ["red", "medium blue", "forest green", "lawn green", "yellow"]        
# def shape(shape_line):
#     angle = 360/ shape_line
#     for _ in range(shape_line):
#         square.forward(100)      
#         square.left(angle)
# for i in range( 3 , 11):
#         shape(i)
#         square.color(random.choices(colour))

import random
direction = [0, 90, 180, 270]
# colour = ["red", "medium blue", "forest green", "lawn green", "yellow", "dodger blue", "medium spring green", "magenta"]
square.speed(0)

colormode(255)
def color_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r , g , b)
    


for i in range(100):
    square.pensize(10)
    square.setheading(random.choice(direction))
    colormode(color_random)
    square.forward(30)

screen_page = Screen()
screen_page.exitonclick()
