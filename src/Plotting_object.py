import matplotlib.pyplot as plt


class SinglePlot(object):

    def __init__(self, title=""):
        figure, ax = plt.subplots(1)
        self.figure = figure
        self.axes = ax

    def plot(self, x, y, label=None):
        if label is None:
            return self.axes.plot(x, y)
        else:
            return self.axes.plot(x, y, label=label)

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

    def set_title(self, title):
        self.axes.set_title(title)

    def remove_line(self, line):
        self.axes.lines.remove(line)


# Multiplot will have multiple axis and will bee implemented later
class MultiPlot(object):

    def __init__(self, row, column, title=""):
        figure, ax = plt.subplots(1)
        self.figure = figure
        self.axes = ax

    def plot(self, x, y, label=None):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

    def set_title(self, label):
        pass
