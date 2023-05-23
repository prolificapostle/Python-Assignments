from math import pi

def area_circle(r):
    try:
        return pi * (r ** 2)
    except (TypeError, ValueError):
        print("Eyes dey pain you ? Enter an integer")

area_circle(y)