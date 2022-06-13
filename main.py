import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
data_state = data["state"].to_list()

guessed_state = []
while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 ", prompt="What's another state's name").title()

    if answer_state in data_state:
        guessed_state.append(answer_state)

        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(state_data.state.item())

screen.exitonclick()















