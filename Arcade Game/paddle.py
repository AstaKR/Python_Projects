from turtle import Turtle, Screen 
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        #paddle Setup
        self.color("white")
        self.shape("square")
        # screen.tracer(0)
        # self.setposition(x=370 , y = 10)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.x_position = self.xcor()
        self.y_position = self.ycor() + 20
        self.goto(x=self.x_position, y=self.y_position)

    def go_down(self):
        self.x_position = self.xcor() 
        self.y_position = self.ycor() - 20
        self.goto(x=self.x_position, y=self.y_position)


    
