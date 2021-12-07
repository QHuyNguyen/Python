from turtle import Turtle

class Scoreboad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("classic")
        self.goto(0, 280)
        self.color("white")
        self.setup()

    def increment(self):
        self.score += 1
        self.clear()
        self.setup()

    def setup(self):
        self.write(f"Score: {self.score}", align="center", move=False, font=("Arial", 8, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", move=False, font=("Arial", 18, "normal"))
        self.hideturtle()