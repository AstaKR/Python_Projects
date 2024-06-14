###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import colorgram
import turtle
kali = turtle
rgb_colors = []
colors = colorgram.extract('D:/PROJECTS/100 days python/hirst-painting-start/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = r , g, b
    rgb_colors.append(new_color)
print (rgb_colors)
kali.speed("fastest")
kali.hideturtle()
kali.penup()
kali.colormode(255)
kali.setheading(220)
kali.forward(250)
num_of_counts = 100
colors_values = [ (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for count in range(1, num_of_counts +1 ):
    kali.setheading(0)
    kali.dot(10, random.choice(colors_values))
    kali.forward(20)
    if count % 10 ==0:
        kali.setheading(90)
        kali.forward(30)
        kali.setheading(180)
        kali.forward(200)
        kali.setheading(0)

kali.pendown()





my_screen = kali.Screen()

my_screen.exitonclick()