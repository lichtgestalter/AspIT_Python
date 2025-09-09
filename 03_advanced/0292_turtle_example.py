import turtle  # this imports a library called "turtle". A library is (typically someone else's) python code, that you can use in your own program.

def demo():  # demonstration of basic turtle commands
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window


tom = turtle.Turtle()  # create an object named tom of type Turtle
demo()
turtle.done()  # keep the turtle window open after the program is done
