from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0,
                                 -1):  # start, stop, step - note that it will stop immediately once it reaches stop value
            # get the coordinates of the segment ahead of the current segment
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            # move the segment to the new coordinates
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def left(self):
        self.head.setheading(180)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)
