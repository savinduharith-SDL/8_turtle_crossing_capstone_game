from turtle import Turtle
from random import randint, choice
START_X_POS = 300
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.setheading(180)
        start_y_pos = randint(-240, 240)
        self.goto(START_X_POS, start_y_pos)
