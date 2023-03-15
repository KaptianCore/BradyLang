import re
from collections import namedtuple

# Define the token structure
Token = namedtuple("Token", ["type", "value"])

# Define token patterns for different language constructs
# To customize the syntax, add or modify the token patterns here
token_patterns = [
    ("NUMBER", r"\d+(\.\d*)?"),
    ("STRING", r"\".*?\""),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("OPERATOR", r"[+\-*/]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("SEMICOLON", r";"),
    ("WHITESPACE", r"\s+"),
    ("ASSIGN", r"->"),
    ("PRINT", r"\bprint\b"),  # New token pattern for the print keyword
    # Add more token patterns as needed
]

# Compile regex patterns
regex_patterns = "|".join(f"(?P<{t}>{p})" for t, p in token_patterns)
token_regex = re.compile(regex_patterns)

def lex(input):
    tokens = []
    for match in re.finditer(token_regex, input):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        token = Token(type=token_type, value=token_value)
        tokens.append(token)

    return tokens

# To add custom file extension support, update the code in main.py where the source code is read
