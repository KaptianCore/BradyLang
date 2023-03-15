from bradylang import lex, parse, Interpreter
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source.bld>")
        return

    source_file = sys.argv[1]
    if not source_file.endswith(".brady"):
        print("Error: Invalid file extension. Expected '.brady'.")
        return

    with open(source_file, "r") as f:
        source_code = f.read()

    tokens = lex(source_code)
    ast = parse(tokens)
    interpreter = Interpreter()
    result = interpreter.interpret(ast)
    print(result)

if __name__ == "__main__":
    main()
