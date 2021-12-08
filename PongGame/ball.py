from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.angle = 30

    def move(self):
        self.setheading(self.angle)
        self.forward(0.3)

    def change_direction(self):
        self.angle += 30
