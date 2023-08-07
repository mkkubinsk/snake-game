from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_LENGTH = 3


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake(START_LENGTH)
        self.head = self.snake[0]

    def create_snake(self, length):
        for i in range(length):
            snake_segment = Turtle(shape='square')
            snake_segment.color('black')
            snake_segment.penup()
            if i != 0:
                snake_segment.setx(self.snake[i - 1].xcor() - 20)
            elif length == 1:
                snake_segment.setpos(self.snake[-1].pos())
            self.snake.append(snake_segment)
            self.snake[-1].color('white')

    def move(self):
        for i in range(len(self.snake) - 1, -1, -1):
            if i > 0:
                self.snake[i].setpos(self.snake[i - 1].pos())
            elif i == 0:
                self.snake[i].forward(MOVE_DISTANCE)

    def restart(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake(START_LENGTH)
        self.head = self.snake[0]

    def turn_up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)
