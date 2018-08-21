def circleArea(radius):
    area=3.142*(radius**2)
    return area

radius=float(input("Enter Radius: "))
print("The area of a circle with radius {}cm is {:.3f}cm~2".format(radius, circleArea(radius)))
