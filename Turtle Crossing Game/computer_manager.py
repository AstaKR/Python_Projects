from turtle import Turtle
import random
COLOURS = ["green", "orange", "blue", "black", "red", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT= 10

class CarManger:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        new_cars = Turtle()
        random_no = random.randrange(1,6)
        if random_no ==1 :
            new_cars.shape("square")
            new_cars.shapesize(stretch_len=2, stretch_wid=1)
            new_cars.penup()
            
            new_cars.color(random.choice(COLOURS))
            random_y = random.randint(-250, 250)
            new_cars.goto(x=280 , y=random_y)
            self.all_cars.append(new_cars)
        
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
        
    def game_level_up(self):
        self.car_speed += MOVE_INCREMENT
    

        