


class Dataset(object):

    def __init__(self, x, y, label):
        self.xdata = x
        self.ydata = y
        self.label = label

    def get_data(self):
        return self.xdata, self.ydata

    def __str__(self):
        return self.label

    def get_plot_label(self):
        return self.label


class FittedData(Dataset):

    def __init__(self, x, y_orig, label, function, params):
        self.y_orig = y_orig
        y = function(x, *params)
        self.function = function
        self.parameters = params
        super(FittedData, self).__init__(x, y, label)

    def get_plot_label(self):
        return self.label+ "_fitted_data"

    def get_diff(self):
        return self.y_orig  - self.ydata

    def get_diff_label(self):
        return self.label + "_diff"

