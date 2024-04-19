import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def write_on_map(state, answer):
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto(int(state.x), int(state.y))
    pen.write(answer, align="left", font=("Courier", 7, "normal"))


data = pandas.read_csv("50_states.csv")
guessed_states = []
# TODO 4. Use a loop to allow the user to keep guessing
while len(guessed_states) < len(data.state):
    # TODO 6. Keep track of the score
    score = len(guessed_states)
    # TODO 1. Convert the guess to Title case
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # TODO 2. Check if the guess is among the 50 states
    checked_state = data[data.state == answer_state]
    if len(checked_state.index) > 0:
        # TODO 3. Write correct guesses onto the map
        write_on_map(checked_state, answer_state)
        # TODO 5. Record the correct guesses in a list
        guessed_states.append(checked_state)
        print(answer_state)

screen.mainloop()
