from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = []
for i in range(3):
    snake_segment = Turtle(shape='square')
    snake_segment.color('white')
    snake_segment.penup()
    if i != 0:
        snake_segment.setx(snake[i - 1].xcor() - 20)
    snake.append(snake_segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake) - 1, -1, -1):
        if i > 0:
            snake[i].setpos(snake[i - 1].pos())
        elif i == 0:
            snake[i].forward(20)

screen.exitonclick()