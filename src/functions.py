import numpy as np


def exponential(x, A0, alpha, C):
    y = A0*np.exp(alpha*x) + C
    return y


def linear(x, m, c):
    y = m*x + c
    return y


def quadratic(x, a, b, c):
    y = a*x*x + b*x + c
    return y


def gaussian(x,x0,w, Area):
    a = Area/(w*np.power(np.pi*2,0.5))
    b = -0.5*np.power(x-x0,2)/np.power(w,2)
    return a*np.exp(b)


def lorentzian(x, x0, w, Area):
    w_squared = np.power(w, 2)
    x_squared = np.power(x-x0, 2)
    l = (0.5 / np.pi) * (w / ((0.25 * w_squared) + (4 * x_squared)))
    return Area*l


#FIT_FUNCTIONS = {"Exponential: a*exp(bx) + c": exponential, "Linear: ax +b": linear,
#                 "Quadratic: ax^2 + bx + c": quadratic}


class Function(object):

    def __init__(self, function_name, call, parameters,  description=""):
        self.name = function_name
        self.call = call
        self._description = description
        self.parameters = parameters

    def __str__(self):
        return self.name

    @property
    def description(self):
        return self._description

    def get_description(self):
        text = self.description + "\n" + str(self.parameters)
        return text

    def __call__(self,*args, **kwargs):
        return self.call(*args, **kwargs)




Exponential = Function("Exponential", exponential, ["A0", "alpha", "C"], "A0*exp(alpha*x) + C")
Linear = Function("Linear", linear, ["m", "c"], "m*x + c")
Quadratic =  Function("Quadratic", quadratic, ["a", "b", "c"], "ax^2 + bx + c")
Gaussian = Function("Gaussian", gaussian, ["x0", "w", "Area"], "x0 -> Center, w -> width, Area -> Area")
Lorentzian = Function("Lorentzian", lorentzian, ["x0", "w", "Area"], "x0 -> Center, w -> width, Area -> Area")





FIT_FUNCTIONS = {"Exponential": Exponential, "Linear": Linear, "Quadratic": Quadratic, "Gaussian": Gaussian,
                 "Lorentzian": Lorentzian}

    