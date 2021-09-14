from turtle import *
from math import sqrt
shape("turtle")
d=200
for i in range (4):
    forward(d)
    left(90)
left(45)
forward(d*sqrt(2))
mainloop()