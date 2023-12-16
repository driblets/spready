from spready import sproute

@sproute(path="/customer/a", method="GET")
def execute(inp1: str): 
    print("Hi")
    return "Hello"
