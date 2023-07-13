from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_over import Game_over
import time


def play_again():
    user_input = screen.textinput(title='Sorry:(',
                             prompt='Play again? type "Y" or "N":')
    if user_input.lower() != "y":
        return False
    else:
        food.reset()
        scoreboard.reset()
        game_over.reset()
        snake.snake.clear()
        screen.reset()
        return True


# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

play = True

while play:
    # Snake setup
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Snake navigation based on key-presses
    screen.listen()
    screen.onkey(key='Up', fun=snake.turn_up)
    screen.onkey(key='Down', fun=snake.turn_down)
    screen.onkey(key='Left', fun=snake.turn_left)
    screen.onkey(key='Right', fun=snake.turn_right)

    # Game loop
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.restart()
            scoreboard.update_score()
            snake.create_snake(1)

        # Detect collision with wall
        snake_abs_x = abs(snake.head.xcor())
        snake_abs_y = abs(snake.head.ycor())
        if snake_abs_x >= 290 or snake_abs_y >= 290:
            game_on = False
            game_over = Game_over()
            play = play_again()

        # Detect collision with tail (using slicing)
        for segments in snake.snake[1:]:
            if snake.head.pos() == segments.pos():
                game_on = False
                game_over = Game_over()
                play = play_again()

screen.exitonclick()
