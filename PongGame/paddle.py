from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.setposition(x=self.pos_x, y=self.pos_y)
        self.color('white')
        self.penup()

    def move_up(self):
        self.pos_y += 30
        self.goto(self.pos_x, self.pos_y)

    def move_down(self):
        self.pos_y -= 30
        self.goto(self.pos_x, self.pos_y)