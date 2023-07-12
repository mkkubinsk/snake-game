from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

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
