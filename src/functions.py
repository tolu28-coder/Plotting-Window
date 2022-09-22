import numpy as np


def exponential(x, a, b, c):
    y = a*np.exp(b*x) + c
    return y


def linear(x, a, b):
    y = a*x + b
    return y

def quadratic(x, a, b, c):
    y = a*x*x + b*x + c
    return y

FIT_FUNCTIONS = {"Exponential: a*exp(bx) + c": exponential, "Linear: ax +b": linear,
                 "Quadratic: ax^2 + bx + c": quadratic}


class Function(object):

    def __init__(self):
        pass
    