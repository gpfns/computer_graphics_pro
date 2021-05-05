import numpy as np
from math import sin, cos, radians as r


def b_t(dx, dy):
    return np.mat([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])


def b_s(sx, sy):
    return np.mat([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


def b_r(theta):
    return np.mat([
        [cos(r(theta)), -sin(r(theta)), 0],
        [sin(r(theta)), cos(r(theta)), 0],
        [0, 0, 1]
    ])


def inp_m(x, y):
    return np.mat([
        [x],
        [y],
        [1]
    ])


def basic_m(points, parameters):
    pass


def b_t_t(x, y):
    l1 = []
    for i in x:
        temp = b_t(y[0], y[1]) * inp_m(i[0], i[1])
        print(temp)
        l1.append(temp)
    return l1


def b_t_s(x, y):
    l1 = []
    for i in x:
        l1.append(b_s(y[0], y[1]) * inp_m(i[0], i[1]))
    return l1


def b_t_r(x, y):
    l1 = []
    for i in x:
        l1.append(b_r(y) * inp_m(i[0], i[1]))
    return l1
