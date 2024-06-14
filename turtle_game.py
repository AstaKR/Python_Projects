import turtle
import random
kali = turtle
screen  = turtle.Screen()
screen.setup(width=400 ,height=400)
user_choice = kali.textinput( title="Make a met" , prompt="""Enter your bet to turtle color: 
('red', 'green', 'blue', 'pink', 'yellow', 'black')
                             """ )
colour = ["red", "green", "blue", "pink", "yellow", "black"]
y_place = [-80 , -40 , 0 , 40 , 80 , 120]
x_place = -180
all_turtle = []

    
    
is_game_on = False
for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=x_place, y=y_place[turtle_index])
    new_turtle.color(colour[turtle_index])
    all_turtle.append(new_turtle)
wining_color = ""

if user_choice :
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 160:
            is_game_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_choice:
                print(f"You win. {wining_color} is win the game ")
            else:
                print(f"You lose. {wining_color} is win the game ")
        random_distance = random.randint(0 , 10)
        turtle.forward(random_distance)


screen.exitonclick()