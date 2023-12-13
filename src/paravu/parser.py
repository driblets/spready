import ast


class ParavuDecoratorParser:
    def __init__(self, directoryPath: str):
        self.directoryPath = directoryPath

    @staticmethod
    def parse_ast(filename):
        with open(filename, "rt") as file:
            return ast.parse(file.read(), filename=filename)

    @staticmethod
    def top_level_functions(body):
        return (f for f in body if isinstance(f, ast.FunctionDef))

    def get_functions(self, filename):
        functions = []
        tree = self.parse_ast(filename)
        for func in self.top_level_functions(tree.body):
            functions.append(func)
        return functions

    def parse(self):
        return self.parseModule("tests/sample.py")
    
    def parseModule(self, filePath: str):
        functions = self.get_functions(filePath)
        for func in functions:
            print(func.name)
            decors = func.decorator_list
            for decor in decors:
                for decor_arg in decor.keywords:
                    print("")
                    print(decor_arg.arg)
                    print(decor_arg.value.value)


# if __name__ == "__main__":
#     p = ParavuDecoratorParser("src").parse()
