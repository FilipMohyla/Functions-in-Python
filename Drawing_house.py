from turtle import forward, left, right, exitonclick
from math import sqrt

def house (wall_lenght):
    """ This function draws house and returns wall lenght defined by given argument"""
    
    for walls in range(4):
        forward(wall_lenght)
        left(90)

    left(45)
    forward(sqrt(2) * wall_lenght)
    
    for roof in range(2):
        left(90)
        forward(sqrt(2) * (wall_lenght/2))
    
    left(90)
    forward(sqrt(2) * wall_lenght)

    exitonclick()
    return wall_lenght

house(89)