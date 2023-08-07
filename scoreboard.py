from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.hideturtle()
        self.sety(260)
        self.pencolor('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data_file:
                # data_file.write(str(self.high_score))
                data_file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1