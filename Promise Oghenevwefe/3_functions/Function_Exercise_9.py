import turtle

def draw_star():
    canvasScreen = turtle.Screen()
    myTurtle = turtle.Turtle()

    for x in range(5):
        myTurtle.forward(100)
        myTurtle.right(144)
        myTurtle.forward(100)

    canvasScreen.mainloop()

draw_star()

