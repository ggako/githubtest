# This is the main program
# test2.py is the library

from test2 import distance 


x1 = float(input('What is the x coordinate of the first point? '))
y1 = float(input('What is the y coordinate of the first point? '))
x2 = float(input('What is the x coordinate of the second point? '))
y2 = float(input('What is the y coordinate of the second point? '))


print(distance(x1, y1, x2, y2))