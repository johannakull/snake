from time import sleep
from turtle import Turtle

SCORE_ALIGNMENT = "left"
SCORE_POS = (-200, 250)
HIGH_SCORE_ALIGNMENT = "right"
HIGH_SCORE_POS = (200, 250)
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.setpos(SCORE_POS)
        self.write(f"Score: {self.score}", align=SCORE_ALIGNMENT, font=FONT)
        self.setpos(HIGH_SCORE_POS)
        self.write(f"High Score: {self.high_score}", align=HIGH_SCORE_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
