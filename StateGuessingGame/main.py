from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title('U.S. State game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.screensize(300, 300)

file = pandas.read_csv('50_states.csv')
list_x = []
list_y = []
for x in file.x:
    list_x.append(x)
for y in file.y:
    list_y.append(y)
#print(list_x)
#print(list_y)
index = 0
dict = {}
for state in file.state:
    dict[state] = [list_x[index], list_y[index]]
    index += 1
is_game_on = True

while is_game_on:
    answer = screen.textinput(title='shit game', prompt='What state bitch')
    text = Turtle()
    text.hideturtle()
    text.penup()
    text.color('black')

    for k, v in dict.items():
        if answer == k.lower():
            print(k)
            print(dict[k][0], dict[k][1])
            text.goto(int(dict[k][0]), int(dict[k][1]))
            text.write(answer, align='center')


screen.exitonclick()
