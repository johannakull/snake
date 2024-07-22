from turtle import Turtle, Screen

SNAKE_STARTING_SIZE = 3
SNAKE_SEGMENT_SIZE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johanna's Snake Game")

snake = []
x_pos = 0

for _ in range(SNAKE_STARTING_SIZE):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.setx(x_pos)
    snake.append(snake_segment)
    x_pos -= SNAKE_SEGMENT_SIZE

# TODO: move snake body
# TODO: steer snake
# TODO: detect collision with food
# TODO: keep track of score
# TODO: detect collision with wall
# TODO: detect snake's collision with itself
screen.exitonclick()
