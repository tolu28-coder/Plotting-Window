import numpy as np


def exponential(x, a, b, c):
    y = a*np.exp(b*x) + c
    return y


FIT_FUNCTIONS = {"Exponential: a*exp(b*x) + c": exponential}