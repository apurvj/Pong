from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.pu()
        self.goto(pos)
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        new_y = self.ycor() + 40
        if self.ycor() < 280:
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        if self.ycor() > -280:
            self.goto(x=self.xcor(), y=new_y)
