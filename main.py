from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

l_pad = Paddle((-370, 0))
r_pad = Paddle((370, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(l_pad.move_up, "w")
screen.onkeypress(l_pad.move_down, "s")
screen.onkeypress(r_pad.move_up, "Up")
screen.onkeypress(r_pad.move_down, "Down")
screen.onkeypress(scoreboard.game_over, "Escape")

while scoreboard.over:
    screen.update()
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    if ball.distance(r_pad) < 45 and ball.xcor() > 350 or ball.distance(l_pad) < 45 and ball.xcor() < -350:
        ball.speed_ball()
        ball.bounce_back()

    if ball.xcor() > 400:
        ball.reset_pos()
        scoreboard.update_l()

    if ball.xcor() < -400:
        ball.reset_pos()
        scoreboard.update_r()

screen.exitonclick()
