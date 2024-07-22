from turtle import Turtle, Screen

SNAKE_STARTING_SIZE = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johanna's Snake Game")

x_pos = 0

for _ in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.setx(x_pos)
    x_pos -= 20

# TODO: move snake body
# TODO: steer snake
# TODO: detect collision with food
# TODO: keep track of score
# TODO: detect collision with wall
# TODO: detect snake's collision with itself
screen.exitonclick()
