from spready import sproute

@sproute(path="/customer/a", methods="GET")
def execute(inp1: str): 
    print("Hi")
    return "Hello"
