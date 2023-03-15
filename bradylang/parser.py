from .lexer import Token

class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, value):
        self.value = value

class Assignment(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class Print(ASTNode):  # New AST node class for print statements
    def __init__(self, expression):
        self.expression = expression

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def _advance(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def parse(self):
        if self.current_token is None:  # Check if there are more tokens
            return None
        elif self.current_token.type == 'PRINT':
            self._advance()
            return self.print_statement()
        else:
            return self.assignment()

    def print_statement(self):
        expression = self.expression()
        return Print(expression)

    def assignment(self):
        identifier = self.current_token
        self._advance()
        self._expect('EQUALS')
        value = self.expression()
        return Assignment(identifier, value)

    def expression(self):
        return self.number()

    def number(self):
        value = self.current_token.value
        self._advance()
        return Number(value)

    def _expect(self, token_type):
        if self.current_token.type == token_type:
            self._advance()
        else:
            raise ValueError(f"Unexpected token. Expected {token_type}, but got {self.current_token.type}")

def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()
