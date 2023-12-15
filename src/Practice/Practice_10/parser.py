from dataclasses import dataclass
from typing import List, Union


@dataclass
class ParseTree:
    name: str
    children: List[Union[str, 'ParseTree']]


def parse_start(tokens, current):
    t_node, current = parse_T(tokens, current)
    sum_node, current = parse_sum(tokens, current)
    if t_node and sum_node:
        return ParseTree("START", [t_node, sum_node]), current
    return None, current


def parse_sum(tokens, current):
    if current < len(tokens) and tokens[current] == "+":
        current += 1
        t_node, current = parse_T(tokens, current)
        sum_node, current = parse_sum(tokens, current)
        if t_node and sum_node:
            return ParseTree("SUM", ["+", t_node, sum_node]), current
        return None, current
    return ParseTree("SUM", ["eps"]), current


def parse_T(tokens, current):
    token_node, current = parse_token(tokens, current)
    prod_node, current = parse_prod(tokens, current)
    if token_node or prod_node:
        return ParseTree("T", [token_node, prod_node]), current
    return None, current


def parse_prod(tokens, current):
    if current < len(tokens) and tokens[current] == "*":
        current += 1
        token_node, current = parse_token(tokens, current)
        prod_node, current = parse_prod(tokens, current)
        if token_node or prod_node:
            return ParseTree("PROD", ["*", token_node, prod_node]), current
        return None, current
    return ParseTree("PROD", ["eps"]), current


def parse_token(tokens, current):
    if current < len(tokens) and tokens[current] == "(":
        current += 1
        start_node, current = parse_start(tokens, current)
        if current < len(tokens) and tokens[current] == ")":
            current += 1
            return ParseTree("TOKEN", ["(", start_node, ")"]), current
        return None, current
    elif current < len(tokens) and tokens[current].isdigit():
        current += 1
        return ParseTree("TOKEN", ["id(" + tokens[current - 1] + ")"]), current
    return None, current


def parse(tokens):
    tree, current = parse_start(tokens, 0)
    if tree and current == len(tokens):
        return tree
    return None


def pretty_print(tree, depth=0):
    if isinstance(tree, ParseTree):
        print("." * depth, tree.name)
        for child in tree.children:
            pretty_print(child, depth + 4)
    else:
        print("." * depth, tree)


# if __name__ == "__main__":
#     input_str = input("Enter the expression: ")
#     tokens = input_str.split()
#     parse_tree = parse(tokens)
#
#     if parse_tree:
#         print("Parse Tree:")
#         pretty_print(parse_tree)
#     else:
#         print("Error in parsing.")
