import importlib
from typing import Any, Dict


def runjob(funcName: str, params: Dict[str, Any]):
    print(f"Running myfunc with {funcName} and {params}")
    function_string = funcName
    mod_name, func_name = function_string.rsplit('.',1)
    mod = importlib.import_module(mod_name)
    func = getattr(mod, func_name)
    return func()
