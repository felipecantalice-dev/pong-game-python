from turtle import Screen
import time

from config import Config
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

# screen config
screen = Screen()
screen.bgcolor("black")
screen.setup(width=Config.WINDOW_WIDTH, height=Config.WINDOW_HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

# game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

# keyboard listener
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

## game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball goes out of bounds(Left point)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if ball goes out of bounds(Right point)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()