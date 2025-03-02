from turtle import Screen, Turtle
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()