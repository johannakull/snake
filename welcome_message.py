from turtle import Turtle

HEADING_FONT = ("Courier", 18, "normal")
BODY_FONT = ("Courier", 16, "normal")

HEADING_POS = (0, 40)
DOUBLE_LINE_BREAK_DISTANCE = 40
LINE_BREAK_DISTANCE = 20
PARAGRAPH_BREAK_DISTANCE = 30


class WelcomeMessage(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(HEADING_POS)
        self.setheading(270)
        self.color("white")
        self.display_heading()
        self.display_body()

    def display_heading(self):
        self.write(f"Welcome to Snake!", align="center", font=HEADING_FONT)

    def display_body(self):
        self.forward(DOUBLE_LINE_BREAK_DISTANCE)
        self.write("To navigate, use the arrow keys.", align="center", font=BODY_FONT)
        self.forward(LINE_BREAK_DISTANCE)
        self.write("To exit, press 'q'.", align="center", font=BODY_FONT)
        self.forward(PARAGRAPH_BREAK_DISTANCE)
        self.write("Ready to play? Press the space bar!", align="center", font=BODY_FONT)

    def hide(self):
        self.clear()
