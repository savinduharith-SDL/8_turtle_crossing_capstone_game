from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
START_POS = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(START_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score} | Level : {self.level}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 10
        self.level += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.home()
        self.write("Game Over", font=FONT, align=ALIGNMENT)
