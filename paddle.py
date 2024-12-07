from turtle import Turtle
from config import Config


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=Config.PADDLE_WIDTH, stretch_len=Config.PADDLE_HEIGHT)
        self.color("white")
        self.penup()
        self.goto(position)
    
    def go_up(self):
        if self.ycor() > 250:
            return
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -250:
            return
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)