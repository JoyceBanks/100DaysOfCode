import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
state = turtle.Turtle()
state.hideturtle()

data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()

x_values = data.x.tolist()
y_values = data.y.tolist()
coordinates = dict(zip(x_values, y_values))
coor_list = list(coordinates.items())

score = 0
guessed_states = []

# TODO: Use a loop to allow the user to keep guessing
while len(guessed_states) < 50:

    # TODO: Convert the guess to Title case
    state_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if state_answer == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # TODO: Save missing states to a csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # TODO: Check if the guess is among the 50 states
    if state_answer in state_list:
        # TODO: Record the correct guesses in a list
        guessed_states.append(state_answer)
        # TODO: Keep track of the score
        score += 1
        state_data = data[data.state == state_answer]
        state.penup()
        state.goto(int(state_data.x), int(state_data.y))
        state.write(state_answer)

