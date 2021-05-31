from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Epic Snake Game")
screen.tracer(0)
"""Turns animation off, only updates with the screen.update() method."""

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
"""The screen listens for key commands, in order to move the snake."""

game_is_on = True

while game_is_on:
    screen.update()
    """Updates the screen every 0.1 seconds after the snake has completed its movement, for smoother graphics."""
    time.sleep(0.1)

    snake.move()

    # Detects collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.point()

    # Detects collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        """Detects whether the snake head (front segment) is within a certain distance of the wall."""
        scoreboard.reset()
        snake.reset()

    # Detects collision with tail.
    for segment in snake.snake_segments[1:]:
        """Any segment apart from the first one, so it doesn't detect collision with itself."""
        if snake.head.distance(segment) < 8:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
