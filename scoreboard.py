from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 265)
        self.write(self.l_score, font=("Courier", 60, "normal"))
        self.goto(50, 265)
        self.write(self.r_score, font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def draw_line(self):
        line = Turtle()
        line_2 = Turtle()
        line.color("white")
        line_2.color("white")
        line.penup()
        line_2.penup()
        line.pensize(5)
        line_2.pensize(5)
        line.goto(x=0, y=290)
        line_2.goto(x=-380, y=280)
        line.setheading(270)

        not_at_end = True

        while not_at_end:
            if line.ycor() != -290:
                line.pendown()
                line.forward(10)
                line.penup()
                line.forward(10)
            else:
                not_at_end = False
            line.hideturtle()

        not_at_end = True

        while not_at_end:
            while not_at_end:
                if line_2.xcor() != 380:
                    line_2.pendown()
                    line_2.forward(10)
                    line_2.penup()
                    line_2.forward(10)
                else:
                    not_at_end = False
                line_2.hideturtle()
