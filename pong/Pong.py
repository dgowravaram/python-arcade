import turtle



# bg:
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # stops window from updating - speed up game

# score
score1 = 0
score2 = 0

# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0) # speed of animation - max
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()  # so there's no line drawn while moving paddle
paddle1.goto(-350, 0)

# paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0) # speed of animation - max
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()  # so there's no line drawn while moving paddle
paddle2.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation - max
ball.shape("square")
ball.color("white")
ball.penup()  # so there's no line drawn while moving paddle
ball.goto(0, 0)
ball.dx = 2 # every time ball moves, it moves by 2 pixels
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0   Player 2: 0", align="center", font=("Courier", 24, "normal"))

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



window.listen() # listen for keyboard inputs


window.onkeypress(paddle1up, "a")   # when the user presses w, call
                                    # paddle1up()


window.onkeypress(paddle1down, "s") # when the user presses s, call
                                    # paddle1down()


window.onkeypress(paddle2up, "Up")  # when the user presses Up arrow,
                                    # call paddle2up()


window.onkeypress(paddle2down, "Down") # when the user presses Down arrow,
                                       # call paddle2down()



# main game loop:
while True:
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
        score1+=1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx*=-1
        score2+=1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # paddle-ball collisions
    if ball.xcor() > 340 and (ball.xcor() < 350) and  (ball.ycor() < paddle2.ycor()+50) and (ball.ycor() > paddle2.ycor()-50):
        ball.setx(340)
        ball.dx*=-1

    if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() > paddle1.ycor()-50) and (ball.ycor() < paddle1.ycor()+50):
        ball.setx(-340)
        ball.dx*=-1
