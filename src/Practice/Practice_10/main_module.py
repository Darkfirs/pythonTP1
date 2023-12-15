from src.Practice.Practice_10.parser import *


def main():
    input_str = input("Enter the expression: ")
    tokens = input_str.split()
    parse_tree = parse(tokens)

    if parse_tree:
        pretty_print(parse_tree)
    else:
        print("Error in parsing.")


if __name__ == "__main__":
    main()