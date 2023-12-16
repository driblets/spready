import importlib
from typing import Any, Dict
from .parser import SpreadyDecoratorParser

parser = SpreadyDecoratorParser("tests")
spreadyModules = parser.spreadyRouts


def runjob(funcName: str, params: Dict[str, Any]):
    print(f"Running myfunc with {funcName} and {params}")
    if funcName in spreadyModules:
        funcName = spreadyModules[funcName]
    function_string = funcName
    print(function_string.rsplit('.',1))
    mod_name, func_name = function_string.rsplit('.',1)
    mod = importlib.import_module(mod_name)
    func = getattr(mod, func_name)
    return func()
