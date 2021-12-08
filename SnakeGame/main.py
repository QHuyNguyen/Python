from turtle import Screen
from food import Food
from Snake import Snake
from scoreboard import Scoreboad
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True

#Create Snake, Food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboad()

wall_top = 250


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increment()
        snake.extend()
        food.move()

    #Detect collision with screen edge
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with snake tail
    new_snake = snake.full_snake[1:len(snake.full_snake)-1]
    for part in new_snake:
        if snake.head.distance(part) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()



"""class Animal:
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print(f'inhale, exhale, number of eye {self.num_eye}')

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print('swimming')
    def breath(self):
        super().breath()
        print('doing this under water')

fish = Fish()
fish.swim()
fish.breath()"""