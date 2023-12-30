from turtle import Turtle
from random import randint
START_X_POS = 300
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("car")
        self.setheading(180)
        start_y_pos = randint(260, -260)
        self.goto(START_X_POS, start_y_pos)
