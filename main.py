import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t1 = turtle.Turtle()
t1.hideturtle()
t1.pu()

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()


def check_position(x):
    dd = data[data["state"] == x]
    dd_x = int(dd["x"])
    dd_y = int(dd["y"])
    dd_x_y = (dd_x, dd_y)
    return dd_x_y


total_states = 50
already_guessed = []
while len(already_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(already_guessed)}/{total_states}",
                                    prompt="What's the name of another state").title()
    if answer_state == "Exit":
        # states that weren't guessed before exit
        missing_states = []
        for state in state_list:
            if state not in already_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list and answer_state not in already_guessed:
        already_guessed.append(answer_state)
        state_position = check_position(answer_state)
        t1.goto(state_position)
        t1.write(answer_state)
