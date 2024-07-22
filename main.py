from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johanna's Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# TODO: steer snake
# TODO: detect collision with food
# TODO: keep track of score
# TODO: detect collision with wall
# TODO: detect snake's collision with itself
screen.exitonclick()
