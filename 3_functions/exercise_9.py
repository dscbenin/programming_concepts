import turtle
def draw_star():
    scr=turtle.Screen()
    star=turtle.Turtle()
    for i in range(5):
        star.forward(150)
        star.right(144)

draw_star()
