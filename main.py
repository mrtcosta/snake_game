from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# CREATE SCREEN
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

def start_game():
    is_on = True
    score.scores = 0
    score.points('no')

    while is_on:

        screen.update()
        time.sleep(0.080)
        snake.move()

        # DID IT EAT THE FOOD?
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.points(got_food='yes')

        # DID IT HIT THE WALL?
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            snake.reset()
            score.game_over()
            is_on = False


        # DID IT HIT ITSELF?
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                snake.reset()
                is_on = False

# KEYS
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkeypress(start_game, "space")

score.menu()

screen.exitonclick()


