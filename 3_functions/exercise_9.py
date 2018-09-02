import turtle

def draw_a_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.left(144)
        t.forward(sz)


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("myStar")

kex = turtle.Turtle()
kex.pensize(3)
kex.color("white")

draw_a_star(kex, 100)



wn.mainloop()
