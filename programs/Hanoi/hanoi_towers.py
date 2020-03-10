#!/usr/bin/python
"""       turtle-example-suite:
         tdemo_minimal_hanoi.py
A minimal 'Towers of Hanoi' animation:
implementation using a tower class, which
is derived from the built-in type list.
Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/22., 0.9, 1-n/20.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    start_time = time.time()
    hanoi(n, t1, t2, t3)
    elapsed_time = time.time() - start_time
    print("Elapsed time: %0.10f seconds of function Quick_Sort()." % elapsed_time)
    write("press STOP button to exit",
          align="center", font=("Courier", 16, "bold"))

def main():
    global t1, t2, t3, n
    n = int(numinput("discs", "Your discs:", 10, minval=1, maxval=10))
    ht(); penup(); goto(0, -225); delay(1);   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(n,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()
