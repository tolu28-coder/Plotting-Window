import threading
from multiprocessing import Process
from queue import Queue


class MyThread(object):
    """
        class to be defined to be used as a mixin class using threadpadding decorator or can be used as a thread object
    """
    _execute_after_thread = []
    _execute_before_thread = []
    _execute_if_error = []
    _execute_if_success = []

    @staticmethod
    def _null():
        raise NotImplementedError

    def __init__(self):
        self._thread = None
        self._queue = Queue()

    @staticmethod
    def add_to_list(func_list, index):
        """Decorator that adds the function to a given list"""
        def actual_decorator(f):
            func_list[index] = f
            return f
        return actual_decorator

    @staticmethod
    def thread_padding_no_return(before, success, if_error, after):
        # use this decorator if object inherits from MyThread class
        def decorator(func):
            def wrapped_func(self, *args, **kwargs):
                self._execute_before_thread[before](self)
                try:
                    func(*args, **kwargs)
                    self._execute_if_success[success](self)

                except Exception as error:
                    self._execute_if_error[if_error](self, error)

                finally:
                    self._execute_after_thread[after](self)

            def thread_wrapped(self, *args, **kwargs):
                args = [self] + list(args)
                thread = threading.Thread(target=wrapped_func, args=args, kwargs=kwargs)
                thread.start()
            return thread_wrapped

        return decorator

    @staticmethod
    def thread_padding_return(before, success, if_error, after):
        # use this decorator if object inherits from MyThread class and returns a value

        def decorator(func):
            def wrapped_func(self, *args, **kwargs):
                self._execute_before_thread[before](self)
                try:
                    return_val = func(self, *args, **kwargs)
                    self._queue.put(return_val)
                    self._execute_if_success[success](self)

                except Exception as error:
                    self._execute_if_error[if_error](self, error)

                finally:
                    self._execute_after_thread[after](self)

            def thread_wrapped(self, *args, **kwargs):
                args = [self] + list(args)
                thread = threading.Thread(target=wrapped_func, args=args, kwargs=kwargs)
                thread.start()

            return thread_wrapped

        return decorator

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

    # start will not work, will fix it later
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