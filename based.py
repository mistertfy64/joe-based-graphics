import turtle
import math
import time

startTime = time.time();
screen = turtle.Screen();
mark = turtle.Turtle();

screen.setup(1000, 700);
screen.title("Base");
screen.tracer(0, 0);
mark.penup();
mark.speed(0);
mark.hideturtle();
mark.pensize(0.1);

def markDot(x, y):
    mark.pendown();
    mark.goto(x, y);
    mark.penup();

def fillRect(x, y, w, h):
    mark.setheading(0);
    for j in range(h):
        currentY = y + j;
        mark.goto(x, currentY);
        for i in range(w):
            currentX = x + i;
            markDot(currentX, currentY);

def traceRect(x, y, w, h):
    mark.setheading(0);
    for j in range(2):
        currentY = y + h*j;
        mark.goto(x, currentY);
        for i in range(w):
            currentX = x + i;
            markDot(currentX, currentY);
    for k in range(2):
        currentX = x + w*k;
        mark.goto(currentX, y);
        for l in range(h):
            currentY = x + l;
            markDot(currentX, currentY);

def fillCircle(x, y, r):
    for j in range(y-r, y+r+1):
        currentY = j - y;
        currentX = math.sqrt(r*r-currentY*currentY);
        markDot(currentX, j);
        markDot(-currentX, j);
    mark.penup();

def traceCircle2(x, y, r):
    for j in range(y-r, y+r+1):
        for i in range(x-r, x+r+1):
            dX = i - x;
            dY = j - y;
            if (dX*dX + dY*dY <= r*r):
                markDot(i, j);

newTime = time.time();
fillCircle(0, 0, 100);
print(time.time() - newTime);
screen.update();
time.sleep(1);

newTime = time.time();
traceCircle2(200, 200, 100);
print(time.time() - newTime);
screen.update();
time.sleep(5);
