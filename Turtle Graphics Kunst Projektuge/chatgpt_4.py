# Make the drawing more intricate, with more details and correct perspective. It should almost look as a pencil drawing of a professional artist.

import turtle

def draw_house(myturtle, x, y, size):
    # Draw house base
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.color("black")
    myturtle.begin_fill()
    for _ in range(4):
        myturtle.forward(size)
        myturtle.right(90)
    myturtle.end_fill()

    # Draw roof
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.begin_fill()
    myturtle.goto(x + size / 2, y + size / 2)
    myturtle.goto(x + size, y)
    myturtle.end_fill()

    # Draw door
    myturtle.penup()
    myturtle.goto(x + size * 0.2, y)
    myturtle.pendown()
    myturtle.setheading(90)
    myturtle.forward(size * 0.6)
    myturtle.right(90)
    myturtle.forward(size * 0.3)
    myturtle.right(90)
    myturtle.forward(size * 0.6)

def draw_birch_tree(myturtle, x, y, trunk_height, canopy_radius):
    # Draw trunk
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.color("brown")
    myturtle.begin_fill()
    myturtle.setheading(90)
    myturtle.forward(trunk_height)
    myturtle.circle(trunk_height / 2, 180)
    myturtle.forward(trunk_height)
    myturtle.end_fill()

    # Draw canopy
    myturtle.penup()
    myturtle.goto(x, y + trunk_height)
    myturtle.pendown()
    myturtle.color("green")
    myturtle.begin_fill()
    myturtle.circle(canopy_radius)
    myturtle.end_fill()

def draw_cloud(myturtle, x, y, size):
    # Draw cloud
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.color("white")
    myturtle.begin_fill()
    for _ in range(5):
        myturtle.circle(size, 60)
        myturtle.left(120)
    myturtle.end_fill()

def draw_grass(myturtle, x, y, length, num_straws):
    # Draw grass
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.color("green")
    myturtle.setheading(90)
    for _ in range(num_straws):
        myturtle.penup()
        myturtle.goto(x, y)
        myturtle.pendown()
        myturtle.forward(length)
        myturtle.right(90)
        myturtle.forward(5)
        myturtle.right(90)

def draw_landscape(myturtle):
    # Draw ground
    myturtle.penup()
    myturtle.goto(-400, -200)
    myturtle.pendown()
    myturtle.color("saddlebrown")
    myturtle.begin_fill()
    myturtle.goto(400, -200)
    myturtle.goto(400, -100)
    myturtle.goto(-400, -100)
    myturtle.goto(-400, -200)
    myturtle.end_fill()

    # Draw sky
    myturtle.penup()
    myturtle.goto(-400, -100)
    myturtle.pendown()
    myturtle.color("lightblue")
    myturtle.begin_fill()
    myturtle.goto(400, -100)
    myturtle.goto(400, 400)
    myturtle.goto(-400, 400)
    myturtle.goto(-400, -100)
    myturtle.end_fill()

    # Draw sun
    myturtle.penup()
    myturtle.goto(-300, 250)
    myturtle.pendown()
    myturtle.color("yellow")
    myturtle.begin_fill()
    myturtle.circle(50)
    myturtle.end_fill()

    # Draw clouds
    draw_cloud(myturtle, -200, 150, 30)
    draw_cloud(myturtle, 100, 200, 40)

    # Draw grass
    draw_grass(myturtle, -400, -100, 20, 20)
    draw_grass(myturtle, -300, -100, 20, 25)
    draw_grass(myturtle, -200, -100, 20, 20)
    draw_grass(myturtle, -100, -100, 20, 25)
    draw_grass(myturtle, 0, -100, 20, 20)
    draw_grass(myturtle, 100, -100, 20, 25)
    draw_grass(myturtle, 200, -100, 20, 20)
    draw_grass(myturtle, 300, -100, 20, 25)
    draw_grass(myturtle, 400, -100, 20, 20)

    # Draw birch trees
    draw_birch_tree(myturtle, -350, -200, 100, 30)
    draw_birch_tree(myturtle, -250, -200, 100, 30)
    draw_birch_tree(myturtle, -50, -200, 100, 30)
    draw_birch_tree(myturtle, 50, -200, 100, 30)
    draw_birch_tree(myturtle, 250, -200, 100, 30)
    draw_birch_tree(myturtle, 350, -200, 100, 30)

    # Draw house
    draw_house(myturtle, -150, -200, 150)

def main():
    myturtle = turtle.Turtle()  # create an object of type Turtle
    myturtle.speed(0)
    draw_landscape(myturtle)
    turtle.done()  # keeps the turtle window open after the program is done

if __name__ == '__main__':  # is this file run as the main program (as opposed to being imported)?
    main()
