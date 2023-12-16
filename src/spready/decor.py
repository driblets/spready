def sproute(func):
    def wrapper(*args, **kwargs):
        print("This is decorator")
        return func(*args, **kwargs)
    return wrapper
