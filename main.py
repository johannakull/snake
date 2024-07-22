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
    for segment in snake:
        segment.forward(40)
    screen.update()
    time.sleep(0.1)

# TODO: steer snake
# TODO: detect collision with food
# TODO: keep track of score
# TODO: detect collision with wall
# TODO: detect snake's collision with itself
screen.exitonclick()
