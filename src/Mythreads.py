import threading
from multiprocessing import Process
from queue import Queue


class MyThread(object):
    """
        class to be defined to be used as a mixin class using threadpadding decorator or can be used as a thread object
    """

    def __init__(self):
        self._thread = None
        self._queue = Queue()


    @staticmethod
    def thread_padding_no_return(func):
        # use this decorator if object inherits from MyThread class
        def wrapped_func(self, *args, **kwargs):
            self.before_thread()
            try:
                func(*args, **kwargs)

            except Exception as error:
                self.incase_of_error(error)

            finally:
                self.after_thread()

        def thread_wrapped(self, *args, **kwargs):
            args = [self] + list(args)
            thread = threading.Thread(target=wrapped_func, args=args, kwargs=kwargs)
            thread.start()

        return thread_wrapped

    @staticmethod
    def thread_padding_return(func):
        # use this decorator if object inherits from MyThread class
        def wrapped_func(self, *args, **kwargs):
            self.before_thread()
            try:
                return_val = func(self, *args, **kwargs)
                self._queue.put(return_val)
                self.thread_success()

            except Exception as error:
                print("In exception")
                self.incase_of_error(error)

            finally:
                self.after_thread()
                self._thread = None

        def thread_wrapped(self, *args, **kwargs):
            args = tuple([self] + list(args))
            self._thread = threading.Thread(target=wrapped_func, args=args, kwargs=kwargs, daemon=True)
            self._thread.start()

        return thread_wrapped

    def before_thread(self):
        raise NotImplementedError

    def after_thread(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def setup(self, before, run, after, incase_of_error):
        self.before_thread = before
        self.run = run
        self.after_thread = after
        self.incase_of_error = incase_of_error

    def start(self):
        # lambda function should be used to pass arguments or should use class attributes
        self.before_thread()

        try:
            thread = threading.Thread(target=self.run)
            thread.start()

        except Exception as e:
            self.incase_of_error(e)

        finally:
            self.after_thread()

    def incase_of_error(self, exception):
        raise NotImplementedError

    def thread_success(self):
        raise NotImplementedError


class Messenger(object):

    def __init__(self):
        self.callback = self._notgiven

    def _notgiven(self):
        raise NotImplementedError("Callback is not given")

    def setup(self, callback):
        self.callback = callback

    def notify(self):
        self.callback()

    def notify_with_args(self, *args, **kwargs):
        self.callback(*args, **kwargs)