import math
from numpy import mean

try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

"""
This tool is used to visualize extended decimals of irrational numbers or created sequences
such as Pi, the Golden Ration, and Euler's constant.

The string of the number is parsed through and each digit is treated as an angle of rotation. 
Through different computations and methods of movement, abstract, fractal, and controlled visualizations
 can be created. """

#---------------------------------------------------
#                   Digits of Pi
#---------------------------------------------------
"""
The below example is a list of Pi's first 10,001 digits (3 + 10,000 decimals). 
See line 84 for how the Turtle Graphic is created and used.
"""

mp.dps = 10000 # set number of decimal digits
pi = str(mp.pi)
pi = pi.replace('.', '')
pi = list(pi)
pi_final = []


for i in range(len(pi)):
    pi_final.append(int(pi[i]))

#---------------------------------------------------
#                  Euler's constant
#---------------------------------------------------
mp.dps = 10000
# pythonic way of calculating euler's constant
e = ((1+(1/100000000))**100000000)
e = str(mp.e)
e = e.replace('.', '')
e = list(e)
e_final = []

for i in range(len(e)):
    e_final.append(int(e[i]))

#---------------------------------------------------
#                 Golden Ratio
#---------------------------------------------------
mp.dps = 10000
# pythonic phi calculation
phi = (1 + 5**.5)/2
phi = str(mp.phi)
phi = phi.replace('.', '')
phi = list(phi)
phi_final = []

for i in range(len(phi)):
    phi_final.append(int(phi[i]))

#---------------------------------------------------
#              Fibonacci Sequence
#---------------------------------------------------
# pythonic fibonacci sequence creation
previous = 1
current = 1
fib_seq = [1, 1]
for i in range(10000):
    fib_seq.append(fib_seq[i] + fib_seq[i + 1])

#---------------------------------------------------
#                    Cube
#---------------------------------------------------
# creates a cube
drawing = [90, 90, 90, 90, 45, 45, 90, 90, 90, 90, 135, 315, 225, 225, 315, 135]
drawing = drawing * 9999

#---------------------------------------------------
#                  Turtle Graphic
#---------------------------------------------------
import turtle
from turtle import *

"""
The below method is used to control what is visualized
"""

def control():
    on_off = input("See graph movement for each digit: T or F\n--> ")
    value = input("Enter the number 1, 2, 3, 4, or 5 to be visualized:\n1. Pi\n2. Euler's Constant\n3. Phi\n4. Cube\n5. Fibonacci's Sequence\n--> ")
    print(type(value))
    if on_off == "T" or on_off.lower() == 't':
        graph = True
    return bool(on_off), value

# colors list used for methods to call on and create paths in rainbow form. best used
# to see path direction

colors = ['red', 'orange', 'gold', 'green', 'blue', 'dark violet']

"""
The below method sets up the window and allows you to establish certain
rules such as turtle speed, tracer on/off, window dimensions, etc.
"""
def start(graph):
    color('black')
    turtle.fillcolor('')
    begin_fill()
    turtle.speed(speed=0)
    turtle.tracer(graph)
    turtle.hideturtle()
    draw = turtle.Turtle()
    # set window
    turtle.screensize(canvwidth=10000, canvheight=10000,
                      bg="black")

"""
The below method calls on pi for the turtle path, and traces in a rainbow color
For all below methods:
1. .pencolor(colors[color]) iterates through the colors list to create rainbow colored paths to track movement.
this can be changed to common color names as well. Ex: turtle.pencolor('magenta') --> whole path is Magenta.
2. forward(x): x is the length each movement will be
3. left(x): typically the value iterated through the value's list of decimals, things like
         - i*36 set each digit 0-9 as an angle of a circle. 10 digits * 36 degrees = 360 degrees accounted for.
         - i*60 sets triangular movement
         - i*90 --> square
         - i*108 --> pentagonal angles
"""

def pi():
    color = 0
    for i in pi_final:
        color = color % 6
        turtle.pencolor(colors[color])
        #turtle.pencolor('magenta')
        # changes movement length
        forward(10)
        left((i*60))
        color += 1
    turtle.pencolor('white')

def e():
    color = 0
    for i in e_final:
        color = color % 6
        turtle.pencolor(colors[color])
        turtle.pencolor('cyan')
        forward(20)
        left((i*108))
        color += 1
    turtle.pencolor('white')

def phi():
    color = 0
    for i in phi_final:
        color = color % 6
        turtle.pencolor(colors[color])
        turtle.pencolor('yellow')
        forward(20)
        left((i*36))
        color += 1
    turtle.pencolor('white')

def fibonacci_sequence():
    color = 0
    for i in fib_seq:
        color = color % 6
        turtle.pencolor(colors[color])
        forward(20)
        left((i*36))
        color += 1

def cube():
    movement = 0
    color = 0
    for i in drawing:
        color = color % 6
        turtle.pencolor(colors[color])
        forward(100)
        left(i)
        color += 1
        movement += 1
    turtle.pencolor('white')

"""
The selection() method can be updated to take any created sequence for visualization. Ensure control() 
has been updated to offer the user the sequence as an option for input.
"""
def selection(x):
    x = int(x)
    if x == 1:
        pi()
    if x == 2:
        e()
    if x == 3:
        phi()
    if x == 4:
        cube()
    if x == 5:
        fibonacci_sequence()

def finish():
    end_fill()
    done()

def main():
    value = control()
    start(value[0])
    selection(value[1])
    print('done :)')

if __name__ == '__main__':
    main()

