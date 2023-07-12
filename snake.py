from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake_segment = Turtle(shape='square')
            snake_segment.color('white')
            snake_segment.penup()
            if i != 0:
                snake_segment.setx(self.snake[i - 1].xcor() - 20)
            self.snake.append(snake_segment)

    def move(self):
        for i in range(len(self.snake) - 1, -1, -1):
            if i > 0:
                self.snake[i].setpos(self.snake[i - 1].pos())
            elif i == 0:
                self.snake[i].forward(MOVE_DISTANCE)
