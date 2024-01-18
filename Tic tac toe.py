def write(data, _move = False):
    """Write data onto turtle screen."""

    if _move:
        t1.speed(1)
        
    t1.penup()
    t1.goto(-300, 0)
    t1.pendown()
    t1.color("#458ad9")
    t1.write(data, font = ("Comic Sans MS", 30, 'bold'), move = _move)
    t1.speed(5)

def draw_board():
    """The the board for game."""

    t1.penup()
    t1.goto(-300, 100)
    t1.pendown()
    t1.fd(600)

    t1.penup()
    t1.goto(-300, -100)
    t1.pendown()
    t1.fd(600)

    t1.rt(90)
    t1.penup()
    t1.goto(100, 300)
    t1.pendown()
    t1.fd(600)

    t1.penup()
    t1.goto(-100, 300)
    t1.pendown()
    t1.fd(600)

def draw_xo(posiiton, symbol):
    """Draw x or o according to symbol."""

    if symbol.casefold() == "x":
        draw_x(posiiton)

    elif symbol.casefold() == "o":
        draw_o(posiiton)

def draw_x(position):
    """Draw x in the board."""

    x = position[0]
    y = position[1]
    
    t1.penup()
    t1.pencolor("#ff4000")
    t1.goto(x, y)
    t1.pendown()

    t1.lt(45)
    t1.fd(100)
    t1.bk(200)
    t1.fd(100)

    t1.rt(90)
    t1.fd(100)
    t1.bk(200)
    t1.fd(100)

    t1.lt(45)

def draw_o(position):
    """Draw o in the board."""

    x = position[0] + 10
    y = position[1]

    t1.penup()
    t1.pencolor("#b800e6")
    t1.goto(x - 100, y)
    t1.pendown()
    t1.circle(90)

def win_checker():
    """Check wheather any player won or not."""

    global point_1
    global point_2

    flag = False

    for I in range(3):
        if game[0][I] == game[1][I] == game[2][I] != " ":

            t1.penup()
            t1.pensize(50)
            t1.pencolor("#3399ff")
            t1.goto(position_data[I + 1][0], 300)
            t1.pendown()
            t1.goto(position_data[I + 1][0], -300)

            write("%s wins" %(player_1 if game[0][I] == "x" else player_2))

            point_1 += 1 if game[0][I] == "x" else 0
            point_2 += 1 if game[0][I] == "o" else 0
            flag = True

        elif game[I][0] == game[I][1] == game[I][2] != " ":

            get_position_data = [1, 4, 7]

            t1.penup()
            t1.pensize(50)
            t1.pencolor("skyblue")
            t1.goto(-300, position_data[get_position_data[I]][1])
            t1.pendown()
            t1.goto(300, position_data[get_position_data[I]][1])

            write("%s wins" %(player_1 if game[I][0] == "x" else player_2))

            point_1 += 1 if game[I][0] == "x" else 0
            point_2 += 1 if game[I][0] == "o" else 0
            flag = True
    
    if game[0][0] == game[1][1] == game[2][2] != " ":
        t1.penup()
        t1.pensize(50)
        t1.pencolor("skyblue")
        t1.goto(-300, 300)
        t1.pendown()
        t1.goto(300, -300)

        write("%s wins" %(player_1 if game[0][0] == "x" else player_2))

        point_1 += 1 if game[0][0] == "x" else 0
        point_2 += 1 if game[0][0] == "o" else 0
        flag = True

    elif game[0][2] == game[1][1] == game[2][0] != " ":
        t1.penup()
        t1.pensize(50)
        t1.pencolor("skyblue")
        t1.goto(300, 300)
        t1.pendown()
        t1.goto(-300, -300)

        write("%s wins" %(player_1 if game[0][2] == "x" else player_2))

        point_1 += 1 if game[0][2] == "x" else 0
        point_2 += 1 if game[0][2] == "o" else 0
        flag = True
    
    return flag

def index(symbol):
    """To insert the selected element for the backend."""

    index = position[number]
    index = position[number]
    game[int(index[0])].pop(int(index[1]))
    game[int(index[0])].insert(int(index[1]), symbol)

def sub_python_inp(symbol):
    """Sub python input getter."""

    for I in range(3):
        temp = [game[0][I], game[1][I], game[2][I]]

        if temp.count(symbol) == 2 and " " in temp:
            return temp.index(" ") * 3 + I + 1

        temp = [game[I][0], game[I][1], game[I][2]]
        
        if temp.count(symbol) == 2 and " " in temp:
            return  I * 3 + temp.index(" ") + 1
        
    temp = [game[0][0], game[1][1], game[2][2]]

    if temp.count(symbol) == 2 and " " in temp:
        return [1, 5, 9][temp.index(" ")]

    temp = [game[0][2], game[1][1], game[2][0]]

    if temp.count(symbol) == 2 and " " in temp:
        return [3, 5, 7][temp.index(" ")]
    
    return False

def python_inp(symbol):
    """Get input from python."""

    from random import choice

    inp_o = sub_python_inp(symbol[0])
    inp_x = sub_python_inp(symbol[1])

    if inp_o:
        return inp_o

    if inp_x:
        return inp_x

    return choice(available)


import turtle

t1 = turtle.Turtle()

turtle.setup(650, 650)
t1.hideturtle()
t1.speed(5)
t1.pensize(10)
t1.clear()
turtle.title("Tic tok toe")

vs_plyr = turtle.textinput("Play v/s?", "Enter correct option, else it will take v/s friend,\nPlay v/s Python(0) or friend(1)?")

if vs_plyr.casefold() in ["python", "0"]:
    choice = turtle.numinput("Player 1 or 2", "Do you wanna be player (1) or (2)?")
    vs_plyr = "Python"

    while choice not in [1, 2]:
        choice = turtle.numinput("Enter correct choice", "Do you wanna be player (1) or (2)?")
    
    name = turtle.textinput("Player", "Hello there!,\nI am python what's your name?").title()

    while name == "Python":
        name = turtle.textinput("Player", "Hey! I am python what's your name?").title()
        
    player_1 = name if choice == 1 else "Python"
    player_2 = name if choice == 2 else "Python"

else:
    player_1 = turtle.textinput("player 1", "Player 1 enter your name.")
    player_2 = turtle.textinput("player 2", "Player 2 enter your name.")

point_1 = 0
point_2 = 0
position = {1 : "00", 2 : "01", 3 : "02", 4 : "10", 5 : "11", 6 : "12", 7 : "20", 8 : '21', 9 : "22"}
position_data = {
    1 : (-200, 200), 
    2 : (0, 200), 
    3 : (200, 200), 
    4 : (-200, 0), 
    5 : (0, 0), 
    6 : (200, 0), 
    7 : (-200, -200), 
    8 : (0, -200), 
    9 : (200, -200)
}
contin = True

while contin:
    t1.home()
    t1.pensize(10)
    t1.pencolor("black")
    t1.clear()
    draw_board()

    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    for I in range(9):
        if I % 2 == 0:
            if player_1 == "Python" and vs_plyr == "Python":
                number = python_inp(["x", "o"])

            else:
                number = turtle.numinput("", "%s enter your position." %player_1)

                while number not in available:
                    number = turtle.numinput("", "%s enter correct position." %player_1)
            
            index("x")
            available.remove(number)
            draw_xo(position_data[number], "x")
        
        else:
            if player_2 == "Python" and vs_plyr == "Python":
                number = python_inp(["o", "x"])

            else:
                number = turtle.numinput("", "%s enter your position." %player_2)

                while number not in available:
                    number = turtle.numinput("", "%s enter correct position." %player_2)
                    
            index("o")
            available.remove(number)
            draw_xo(position_data[number], "o")
            
        if win_checker():
            break

    else:
        write("Game Draws.\n both %s and %s wins." %(player_1, player_2))

    turtle.title("Tic tok toe %s - %d v/s %s - %d" %(player_1, point_1, player_2, point_2))

    contin = turtle.textinput("Continue.", "Wanna continue?").casefold() in ["", "yes", "y", "continue"]

else:
    from time import sleep

    t1.clear()
    t1.pensize(10)
    turtle.title("Programmed by, Gokulakannan")

    if point_1 == point_2:
        write("Ultimately, Game Draws", True)

    else:
        write("Ultimately,\n%s wins" %(player_1 if point_1 > point_2 else player_2), True)

turtle.mainloop()