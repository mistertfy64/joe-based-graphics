from base import *
import turtle
import math
import time

screen.setup(1280, 720);
screen.title("Example");
screen.tracer(0, 0);


fillRect(0, 0, 50, 70);
traceRect(100, 0, 50, 70);
traceCircle(-90, -90, 90);
screen.update();
input();
