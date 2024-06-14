from turtle import Turtle

FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.level_print()

    def level_print(self):
        self.write(f"Level : {self.value} " , align="left", font=FONT)

    def level_increment(self):
        self.clear()
        self.value += 1
        self.level_print()

    def game_over_print(self):
        self.goto(0,0)
        self.write("Game Over", align="Center", font=FONT)
