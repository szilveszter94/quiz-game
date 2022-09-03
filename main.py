import pandas
import turtle
# Setting up Turtle module
turtle_object = turtle.Turtle()
turtle_object.hideturtle()
turtle_object.penup()
screen = turtle.Screen()
screen.setup(width=768, height=768)
screen.bgpic("madar.gif")
# reading data and create arrays
data = pandas.read_csv("madar_nevek.csv")
data_list = data.names.to_list()
correct_names = []
game = True
names_to_learn = []
result = 0
# starting the game with an infinite loop
while game:
    quiz_question = screen.textinput(title=f"Elért eredmény: {result}/9", prompt=("Írd be a madár nevét: \nHa nincs már "
                                                                             "tipped, írd "
                                                                             "be: Feladom")).lower()
    # checking the answer, if it's correct the program write the names with black
    if quiz_question in data_list and quiz_question not in correct_names:
        correct_names.append(quiz_question)
        coordinates = data[data.names == quiz_question]
        turtle_object.goto(int(coordinates.x), int(coordinates.y))
        turtle_object.color("black")
        turtle_object.pencolor("black")
        turtle_object.write(arg=quiz_question, align="center", font=("Impact", 20, "normal"))
        result += 1
        # if 9 answers is correct, is game over
    if result == 9:
        turtle_object.color("magenta")
        turtle_object.goto(-200, 0)
        turtle_object.write(arg="Gratulálok, nyertél!", align ="left", font=("Impact", 40, "bold"))
        # if the player choose surrender, the program write the names with red
        break
    if quiz_question == "feladom":
        for i in data_list:
            if i not in correct_names:
                turtle_object.color("red")
                tanulando_koord = data[data.names == i]
                turtle_object.goto(int(tanulando_koord.x), int(tanulando_koord.y))
                turtle_object.write(arg=i, align="center", font=("Impact", 20, "normal"))
        break

screen.mainloop()
