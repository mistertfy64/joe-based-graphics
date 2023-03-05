import math
import turtle
import time

screen = turtle.Screen();
mark = turtle.Turtle();

"""
screen.setup(1280, 720);
screen.title("base");
screen.tracer(0, 0);
"""

mark.penup();
mark.speed(0);
mark.hideturtle();
mark.pensize(0);

def fillRect(x, y, w, h):
    for j in range(h):
        currentY = y + j;
        mark.pendown();
        mark.goto(x, currentY);
        mark.goto(x + w, currentY);
        mark.penup();

def traceRect(x, y, w, h):
    for j in range(2):
        currentY = y + h*j;
        mark.goto(x, currentY);
        mark.pendown();
        mark.goto(x + w, currentY);
        mark.penup();
    for i in range(2):
        currentX = x + w*i;
        mark.goto(currentX, y);
        mark.pendown();
        mark.goto(currentX, y + h);
        mark.penup();

def traceCircle(x, y, r):
    for j in range(y,  y + r + 1):
        dY = j - y;
        offset = math.sqrt(r*r - dY*dY);
        mark.goto(x + offset, j);
        mark.dot(1);
        mark.goto(x - offset, j);
        mark.dot(1);
        mark.goto(x + offset, y - dY);
        mark.dot(1);
        mark.goto(x - offset, y - dY);
        mark.dot(1);
