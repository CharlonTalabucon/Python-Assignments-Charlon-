#Email: CHARLON.TALABUCON17@myhunter.cuny.edu
#Date: April 11, 2022
#This program prints: A triangle and nestedTriangle turtle loop

import turtle
def setup(t, dist):
    t.penup()
    t.forward(dist)
    t.pendown()

def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)

def main():
    n = int(input("Enter edge length:"))
    
    ned = turtle.Turtle()
    setup(ned, 100)
    triangle(ned, n)

    stark = turtle.Turtle()
    setup(stark, 300)
    nestedTriangle(stark, n)

main()
    
