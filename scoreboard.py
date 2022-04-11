from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.over = True
        self.l_score = 0
        self.r_score = 0
        self.l_pos = (-100, 200)
        self.r_pos = (100, 200)
        self.update()

    def update(self):
        self.clear()
        self.goto(self.l_pos)
        self.write(arg=self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(self.r_pos)
        self.write(arg=self.r_score, align="center", font=("Courier", 60, "normal"))

    def update_r(self):
        self.r_score += 1
        self.update()

    def update_l(self):
        self.l_score += 1
        self.update()

    def game_over(self):
        self.clear()
        if self.l_score > self.r_score:
            self.home()
            self.write(arg="The winner is Player 1", align="center", font=("Courier", 40, "normal"))
        else:
            self.home()
            self.write(arg="The winner is Player 2", align="center", font=("Courier", 40, "normal"))
        self.over = False
