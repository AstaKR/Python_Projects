from turtle import Turtle
FONT = ("Airal", 18, "normal")
ALIGNMENT = "center"
class ScoreBoard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        # PROJECTS/100 days python/SNAKE GAME/data.txt
        with open("./100 days python/SNAKE GAME/data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}        High Score : {self.high_score}" , align = ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("PROJECTS/100 days python/SNAKE GAME/data.txt", mode="w") as high_score:
                high_score.write(f"{self.score}")
        self.score = 0
        self.update_score()
    # def game_over(self):
    #        self.goto(0,0)
    #        self.write("GAME OVER " , align = ALIGNMENT, font=FONT)
    def incerese_score(self):
        self.score += 1
        self.update_score()