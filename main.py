from food import Food
from snake import Snake
from scoreboard import Scoreboard
from time import sleep
from turtle import Screen, bye
from welcome_message import WelcomeMessage


def play_game():
    welcome_message.hide()

    snake = Snake()
    food = Food()

    game_is_on = True

    while game_is_on:
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

        screen.update()
        sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            for segment in snake.segments:
                while segment.distance(food) < 15:
                    food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Johanna's Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()

welcome_message = WelcomeMessage()
screen.update()

screen.listen()
screen.onkey(play_game, "space")
screen.onkey(bye, "q")

screen.exitonclick()
