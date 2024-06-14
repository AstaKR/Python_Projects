from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time
#screen setup

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Game ")
screen.tracer(0)
r_paddle = Paddle((370 , 10))
l_paddle = Paddle((-370, 10))
ball = Ball()
scorebaord = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "x")
screen.onkey(l_paddle.go_down, "c")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.move_speed * 1

    if ball.xcor() > 380 :
        ball.reset_position()
        scorebaord.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scorebaord.r_point()
screen.exitonclick()
