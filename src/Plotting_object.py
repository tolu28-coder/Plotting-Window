import matplotlib.pyplot as plt


class SinglePlot(object):
    
    def __init__(self, title=""):
        figure, ax = plt.subplots(1)
        self.figure = figure
        self.axes = ax
    
    def plot(self, x, y, label=None):
        if label is None:
            self.axes.plot(x, y)
        else:
            self.axes.plot(x, y, label=label)
    
    def set_xlabel(self, label):
        pass
    
    def set_ylabel(self, label):
        pass
    
    def set_title(self, title):
        self.axes.set_title(title)


class MultiPlot(object):
    
    def __init__(self, row, column, title=""):
        figure, ax = plt.subplots(1)
        self.figure = figure
        self.axes = ax
    
    def plot(x, y, label=None):
        pass
    
    def set_xlabel(label):
        pass
    
    def set_ylabel(label):
        pass
    
    def set_title(label):
        pass
    