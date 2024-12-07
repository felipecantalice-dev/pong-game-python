from turtle import Turtle
from config import Config

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = Config.BALL_SPEED

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = Config.BALL_SPEED
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_speed(self):
        self.move_speed *= Config.BALL_MOVE_INCREMENT

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= Config.BALL_MOVE_INCREMENT