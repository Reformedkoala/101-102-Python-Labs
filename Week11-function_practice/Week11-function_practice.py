#  Garrett Thompson
#  CSCI 102 – Section A
#  Week 11 Lab
#  References:
#  Time: 25 minutes
import math


def print_output(input_str):
    print(f'OUTPUT {input_str}')


def triangle_hypotenuse(a, b):
    c = a**2 + b**2
    c = math.sqrt(c)
    print(f'OUTPUT {c:.2f}')


def feet_to_meters(feet):
    meters = feet * .3048
    print(f'OUTPUT {meters:.4f}')


def dollars_to_euros(dollars):
    euros = dollars * .86
    print(f'OUTPUT {euros:.2f}')


def polar_coords(x, y):
    r = x**2 + y**2
    r = math.sqrt(r)
    theta = math.acos((x / r))
    theta = math.degrees(theta)
    print(f'OUTPUT r: {r:.2f}')
    print(f'OUTPUT theta: {theta:.2f}')


