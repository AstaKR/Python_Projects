from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.x_pos = 10
        self.y_pos = 10
        self.move_speed = 0.1

    def move(self):
        self.penup()
        x_pos = self.xcor() + self.x_pos
        y_pos = self.ycor() + self.y_pos
        self.goto(x=x_pos, y=y_pos)

    def bounce_y(self):
        self.y_pos *= -1
    
    def bounce_x(self):
        self.x_pos *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()