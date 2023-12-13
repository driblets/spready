from paravu import papp

@papp(path="/sample", method="GET")
def execute(inp1: str): 
    print("Hi")
    return "Hello"