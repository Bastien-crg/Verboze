from verboze_parser import parser
from environment import Environment


def evaluate(node):
    # If the node is just a number or a string (variable name), return it
    if isinstance(node, int):
        return node
    if isinstance(node, str):
        return node
    if isinstance(node, bool):
        return node

    tag = node[0]

    if tag == 'IF-STMT':
        _, condition, body = node
        if evaluate(condition):
            for stmt in body:
                evaluate(stmt)

    elif tag == 'IF-ELSE-STMT':
        _, condition, if_body, else_body = node
        if evaluate(condition):
            for stmt in if_body:
                evaluate(stmt)
        else:
            for stmt in else_body:
                evaluate(stmt)

    elif tag == 'ASSIGN':
        _, name, expr = node
        env.assign(name,evaluate(expr))

    elif tag == 'DECL':
        _, name, expr = node
        env.define(name,evaluate(expr))

    elif tag == 'DISPLAY':
        _, body = node
        print(body)



if __name__ == '__main__':

    env = Environment()
    # Example AST generated from the parser
    ast = parser.parse('if 0 then { variable a worth 2; display "toto";}')


    for statement in ast:
        evaluate(statement)

    print(env.values)  # Output: {'x': 1, 'y': 2}