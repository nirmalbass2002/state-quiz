import turtle
import pandas

screen=turtle.Screen()
screen.title("us.game")
image=("blank_states_img.gif")
screen.addshape(image)
data=pandas.read_csv("50_states.csv")


turtle.shape(image)

states=data.state.to_list()

correct_ans=[]
while len(correct_ans)<50:
    answer = screen.textinput(title=f"{len(correct_ans)}/50", prompt="what's another state's name?").title()
    if answer=="Exit":
        missing_state=[]
        for state in states:
            if state not in correct_ans:
                missing_state.append(state)
                new_data=pandas.DataFrame(missing_state)
                new_data.to_csv("missing")
        print(missing_state)
        break
    if answer in states :
        correct_ans.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        valid_state=(data[data.state==answer])
        x=(valid_state['x'].iloc[0])
        y=(valid_state['y'].iloc[0])
        t.goto(x,y)
        t.write(answer)
        print(x,y)
screen.exitonclick()
