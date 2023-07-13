from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.sety(260)
        self.pencolor('white')
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)
