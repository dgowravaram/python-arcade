import turtle


# bg:
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # stops window from updating - speed up game

#window.addshape("startbutton.gif")
#start.shape("startbutton.gif")

#window.register_shape("health heart2.gif", shape=None)
#window.addshape("health heart2.gif", shape=None)

title_ = turtle.Turtle()
title_.color("white")
title_.penup()
title_.hideturtle()
title_.goto(0, 140)
title_.pendown()
title_.write("PONG", align="center", font=("Silkscreen", 60, "normal"))

quitButton = turtle.Turtle()
quitButton.color("white")
quitButton.penup()
quitButton.hideturtle()
#quitButton.goto(0, -80)
#quitButton.pendown()
#quitButton.write("QUIT", align="center", font=("Silkscreen", 30, "normal"))aa

start = turtle.Turtle()
start.color("red")
start.penup()
start.hideturtle()
start.goto(0, -50)
start.pendown()
start.write("START", align="center", font=("Silkscreen", 30, "normal"))

instructions = turtle.Turtle()
instructions.color("grey")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -200)
instructions.pendown()
instructions.write("Use up and down arrows to move right paddle", align="center", font=("Silkscreen", 20, "normal"))
instructions.penup()
instructions.goto(0, -250)
instructions.pendown()
instructions.write("Use 'a' and 's' keys to move left paddle", align="center", font=("Silkscreen", 20, "normal"))

def goodbye():
    window.bye()


# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)  # speed of animation - max
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()  # so there's no line drawn while moving paddle
paddle1.goto(-350, 0)

# paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)  # speed of animation - max
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()  # so there's no line drawn while moving paddle
paddle2.goto(350, 0)

def paddle1up():
    y = paddle1.ycor()
    y+=20 # adding 20 pixels to y coordinate
    paddle1.sety(y)

def paddle1down():
    y = paddle1.ycor()
    y-=20 # subtracting 20 pixels to y coordinate
    paddle1.sety(y)

def paddle2up():
    y = paddle2.ycor()
    y+=20 # adding 20 pixels to y coordinate
    paddle2.sety(y)

def paddle2down():
    y = paddle2.ycor()
    y-=20 # subtracting 20 pixels to y coordinate
    paddle2.sety(y)

def runMain(x, y):
    title_.clear()
    quitButton.clear()
    start.clear()
    instructions.clear()
    # num of lives
    # score1 = 0
    # score2 = 0
    lives = 3


    # ball
    ball = turtle.Turtle()
    ball.speed(100)  # speed of animation - max
    ball.shape("square")
    ball.color("white")
    ball.penup()  # so there's no line drawn while moving paddle
    ball.goto(0, 0)
    ball.dx = 2  # every time ball moves, it moves by 2 pixels
    ball.dy = -2

    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    # pen.write("Player 1: 0   Player 2: 0", align="center", font=("Courier", 24, "normal"))

    window.listen() # listen for keyboard inputs
    window.onkeypress(paddle1up, "a")   # when the user presses a, call
                                    # paddle1up()
    window.onkeypress(paddle1down, "s") # when the user presses s, call
                                    # paddle1down()
    window.onkeypress(paddle2up, "Up")  # when the user presses Up arrow,
                                    # call paddle2up()
    window.onkeypress(paddle2down, "Down") # when the user presses Down arrow,
                                       # call paddle2down()



    # main game loop:
    pen.write("Lives left: 3", align="center", font=("Silkscreen", 24, "normal"))
    while(x):
        #pen.write("Lives left: 3", align="center", font=("Silkscreen", 24, "normal"))
        #while True:
        window.update()

        # shift ball's pixels:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # create bounds for ball
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy*=-1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy*=-1

        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx*=-1
            lives = lives-1
            pen.clear()
            pen.write("Lives left: {}".format(lives), align="center", font=("Silkscreen", 24, "normal"))

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx*=-1
            lives = lives-1
            pen.clear()
            pen.write("Lives left: {}".format(lives), align="center", font=("Silkscreen", 24, "normal"))

        # paddle-ball collisions
        if ball.xcor() > 340 and (ball.xcor() < 350) and  (ball.ycor() < paddle2.ycor()+50) and (ball.ycor() > paddle2.ycor()-50):
            ball.setx(340)
            ball.dx*=-1

        if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() > paddle1.ycor()-50) and (ball.ycor() < paddle1.ycor()+50):
            ball.setx(-340)
            ball.dx*=-1

        if lives==0:
            pen.clear()
            paddle1.hideturtle()
            paddle1.clear()
            paddle2.hideturtle()
            paddle2.clear()
            ball.hideturtle()
            ball.clear()
            pen.hideturtle()
            pen.goto(0, 100)
            pen.write("YOU LOST!", align="center", font=("Silkscreen", 60, "normal"))
            pen.hideturtle()
            for i in range(1000):
                pen.goto(0, -i*10)
                pen.write("     ")
            window.bye()




window.onscreenclick(runMain)

turtle.done()
