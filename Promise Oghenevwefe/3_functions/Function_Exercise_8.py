#Write a function area_of_circle(r) which returns the area of circle of radius r

#function for area of circle 
def area_of_circle(r):
    pi = 3.149
    area = pi * (r**2)
    return area


print("The area of circle of radius 5 is: " + str(round(area_of_circle(5), 2)))
