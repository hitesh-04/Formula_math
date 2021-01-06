import math
import cv2

PI = math.pi


def welcome():
    print("Type:\n\t 'r' to put Radius \n\t 'd' to put Diameter \n\t 'c' to put Circumference \n\t 'a' to put Area")

    rd = str(input("\t: "))

    if rd == "r":
        radius()
        welcome()

    if rd == "d":
        diameter()
        welcome()

    if rd == "c":
        circumference()
        welcome()

    if rd == "a":
        area()
        welcome()

    else:
        print("\t  Wrong Input... \n\tPlease! Try Again?")
        welcome()

def radius():
    r = int(input("Put Radius: "))
    dia = r * 2
    circum1 = 2 * PI * r
    area1 = PI * r * r
    print("Circle:\t", "\n\tRadius: ", r, "\n\tDiameter: ", dia, "\n\tCircumference: ", circum1, "\n\tArea:", area1)


def diameter():
    d = int(input("Put Diameter: "))
    r = d / 2
    dia = r * 2
    circum2 = 2 * PI * r
    area2 = PI * r * r
    print("Circle:\t", "\n\tRadius: ", r, "\n\tDiameter: ", dia, "\n\tCircumference: ", circum2, "\n\tArea:", area2)


def circumference():
    circum3 = int(input("Put Circumference: "))
    dia = circum3 / PI
    r = dia / 2
    area3 = PI * r * r
    print("Circle:\t", "\n\tRadius: ", r, "\n\tDiameter: ", dia, "\n\tCircumference: ", circum3, "\n\tArea:", area3)


def area():
    area4 = int(input("Put Area: "))
    root_area = math.pow(area4, 0.5)
    r = root_area / PI
    dia = r * 2
    circum4 = 2 * PI * r
    print("Circle:\t", "\n\tRadius: ", r, "\n\tDiameter: ", dia, "\n\tCircumference: ", circum4, "\n\tArea:", area4)


welcome()
