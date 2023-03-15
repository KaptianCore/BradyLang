from .parser import Number, Identifier, Assignment, Print

class Interpreter:
    def __init__(self):
        self.environment = {}

    def interpret(self, ast):
        self.evaluate(ast)
        return self.environment

    def evaluate(self, node):
        if isinstance(node, Number):
            return float(node.value)
        elif isinstance(node, Identifier):
            return self.environment[node.value]
        elif isinstance(node, Assignment):
            value = self.evaluate(node.value)
            self.environment[node.identifier.value] = value
        elif isinstance(node, Print):  # New evaluation logic for Print node
            print(self.evaluate(node.expression))
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")

def interpret(ast):
    interpreter = Interpreter()
    return interpreter.interpret(ast)