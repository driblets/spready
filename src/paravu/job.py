def myfunc(key: str, value: str):
    print(f"Running myfunc with {key} and {value}")
    return f"{key.replace("/", ".")} => {value}"