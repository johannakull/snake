from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johanna's Snake Game")
screen.tracer(0)

snake = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)
    snake.append(snake_segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment_num in range(len(snake) - 1, 0, -1): # start, stop, step - note that it will stop immediately once it reaches stop value
        # get the coordinates of the segment ahead of the current segment
        new_x = snake[segment_num - 1].xcor()
        new_y = snake[segment_num - 1].ycor()
        # move the segment to the new coordinates
        snake[segment_num].goto(new_x, new_y)
    snake[0].forward(20)

# TODO: steer snake
# TODO: detect collision with food
# TODO: keep track of score
# TODO: detect collision with wall
# TODO: detect snake's collision with itself
screen.exitonclick()
