from functools import wraps
import functools

# def sproute(path, method):
#     ...


class sproute(object):
    def __init__(self, path, method):
        self.path = path
        self.method = method

    def __call__(self, original_func):
        decorator_self = self

        def wrappee(*args, **kwargs):
            print("in decorator before wrapee with flag ", decorator_self.path)
            return original_func(*args, **kwargs)
            print("in decorator after wrapee with flag ", decorator_self.path)

        return wrappee


# @sproute(path="/abc", method="b")
# def bar():
#     print("Running app")


# bar()

# def sproute(f_py=None, path="/", method="GET"):
#     assert callable(f_py) or f_py is None
#     def _decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             kwargs["path"] = path
#             kwargs["method"] = method
#             return func(*args, **kwargs)
#         return wrapper
#     return _decorator(f_py) if callable(f_py) else _decorator


# def sproute(func):
#     def wrapper(*args, **kwargs):
#         print("This is decorator")
#         return func(*args, **kwargs)

#     return wrapper


# def sproute(path, method):
#     def wrapper(config):
#         print("This is decorator")
#         return config

#     return wrapper
