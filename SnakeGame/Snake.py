from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.full_snake = []
        self.x = 0
        self.y = 0
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_part(self.x, self.y)

    def move(self):
        for i in range(len(self.full_snake) - 1, 0, -1):
            x = self.full_snake[i - 1].xcor()
            y = self.full_snake[i - 1].ycor()
            self.full_snake[i].goto(x, y)
        self.full_snake[0].forward(MOVE_DISTANCE)

    def add_part(self, x, y):
        snake = Turtle("square")
        snake.goto(self.x, self.y)
        snake.penup()
        snake.color("white")
        self.full_snake.append(snake)
        self.x -= 20

    def extend(self):
        self.add_part(self.full_snake[-1].xcor(), self.full_snake[-1].ycor())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)