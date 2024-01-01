


class Dataset(object):

    def __init__(self, x, y, label):
        self.xdata = x
        self.ydata = y
        self.label = label
        self.fit = None
        self.is_plotted = True
        self.plot_fitted = False

    def get_data(self):
        return self.xdata, self.ydata

    def __str__(self):
        return self.label

    @property
    def plot_label(self):
        return self.label

    @property
    def is_fitted(self):
        return bool(self.fit)

    @property
    def fitted_data(self):
        if self.fit is None:
            raise Exception("Fitted data does not exist for" + self.label)
        else:
            return self.fit

    @property
    def is_plot_fitted(self):
        return self.plot_fitted



class FittedData(Dataset):

    def __init__(self, x, y_orig, label, function, params, perr):
        self.y_orig = y_orig
        y = function(x, *params)
        self.function = function
        self.parameters = params
        self.perr = perr
        super(FittedData, self).__init__(x, y, label)

    @property
    def plot_label(self):
        return self.label+ "_fitted_data"


    def get_diff(self):
        return self.y_orig  - self.ydata

    @property
    def diff_label(self):
        return self.label + "_diff"

    @property
    def uncertainty(self):
        return self.perr

    @property
    def is_fitted(self):
        #return bool(self.fit)
        NotImplementedError()

    @property
    def fitted_data(self):
        #if self.fit is None:
            #raise Exception("Fitted data does not exist")
        #else:
            #return self.fit
        NotImplementedError()

    def get_parameters(self):
        params = self.function.parameters
        text = ""
        for i in range(len(params)):
            a = "{}: {:4.3f} \n".format(params[i], self.parameters[i])
            text += a
        text = text[:-1]
        return text

    def get_errors(self):
        params = self.function.parameters
        text = ""
        for i in range(len(params)):
            a = "{}: {:4.3f} \n".format(params[i], self.perr[i])
            text += a
        text = text[:-1]
        return text

