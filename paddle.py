from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setx(x)
        self.sety(y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)