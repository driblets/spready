def papp(func):
    def wrapper():
        print("This is decorator")
        func()

    return wrapper()
