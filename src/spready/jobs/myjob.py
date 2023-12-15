from spready import papp

@papp(path="/path")
def execute(): 
    print("Hi")
    return "Hello"

if __name__ == "__main__":
    execute()