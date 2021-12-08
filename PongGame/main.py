from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

is_game_on = True
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()


screen.listen()

screen.onkey(fun=paddle_left.move_up, key='w')
screen.onkey(fun=paddle_left.move_down, key='s')
screen.onkey(fun=paddle_right.move_up, key='Up')
screen.onkey(fun=paddle_right.move_down, key='Down')

while is_game_on:
    if ball.xcor() > 350 or ball.xcor() < -350 or ball.ycor() > 350 or ball.ycor() < -350:
        ball.change_direction()
    if ball.distance(paddle_left) < 10:
        ball.change_direction()
    if ball.distance(paddle_right) < 10:
        ball.change_direction()

    ball.move()


    screen.update()



screen.exitonclick()

