import ply.yacc as yacc
from environment import Environment
from verboze_lexer import tokens

env = Environment()



#
#
#
# def p_block(p):
#     """block : '{' sequence '}'"""



def p_sequence(p):
    """sequence : declaration
                | sequence declaration"""


def p_declaration(p):
    """declaration : VARIABLE ID WORTH expression SEMICOLON
                   | VARIABLE ID SEMICOLON
                   | statement"""

    if len(p) == 6:
        env.define(p[2], p[4])


    elif len(p) == 4:
        env.define(p[2], None)





def p_statement(p):
    """statement : expression SEMICOLON
                 | DISPLAY expression SEMICOLON
                 | if_statement"""

    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 4:
        print(p[2])
        p[0] = None

def p_if_statement(p):
    """if_statement : IF expression THEN statement"""
#                   | IF expression THEN statement ENDTHEN ELSE if_statement"""
    if len(p) == 5:
        if p[2]:
            print("here")
            p[0] = p[4]

    elif len(p) == 7:
        if p[2]:
            p[0] = p[4]
        else:
            p[0] = p[7]


def p_expression(p):
    """expression : assignment"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : logical_or
                  | ID WORTH assignment"""
    if len(p) == 4:
        env.assign(p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]


def p_logical_or_or(p):
    'logical_or : logical_or OR logical_and'
    p[0] = p[1] or p[3]

def p_logical_or_logical_and(p):
    'logical_or : logical_and'
    p[0] = p[1]

def p_logical_and_and(p):
    'logical_and : logical_and AND equality'
    p[0] = p[1] and p[3]

def p_logical_and_equality(p):
    'logical_and : equality'
    p[0] = p[1]

def p_equality_equal(p):
    'equality : equality EQUAL relational'
    p[0] = p[1] == p[3]

def p_equality_ne(p):
    'equality : equality NE relational'
    p[0] = p[1] != p[3]

def p_equality_relational(p):
    'equality : relational'
    p[0] = p[1]

def p_relational_lte(p):
    'relational : relational LTE additive'
    p[0] = p[1] <= p[3]

def p_relational_gte(p):
    'relational : relational GTE additive'
    p[0] = p[1] >= p[3]

def p_relational_lt(p):
    'relational : relational LT additive'
    p[0] = p[1] < p[3]

def p_relational_gt(p):
    'relational : relational GT additive'
    p[0] = p[1] > p[3]

def p_relational_additive(p):
    'relational : additive'
    p[0] = p[1]

def p_additive_minus(p):
    'additive : additive MINUS multiplicative'
    p[0] = p[1] - p[3]

def p_additive_plus(p):
    'additive : additive PLUS multiplicative'
    p[0] = p[1] + p[3]

def p_additive_multiplicative(p):
    'additive : multiplicative'
    p[0] = p[1]

def p_multiplicative_times(p):
    'multiplicative : multiplicative TIMES unary'
    p[0] = p[1] * p[3]

def p_multiplicative_div(p):
    'multiplicative : multiplicative DIVIDE unary'
    p[0] = p[1] / p[3]

def p_multiplicative_unary(p):
    'multiplicative : unary'
    p[0] = p[1]

def p_unary_minus(p):
    'unary : MINUS unary'
    p[0] = -p[2]

def p_unary_not(p):
    'unary : NOT unary'
    p[0] = not p[2]

def p_unary_primary(p):
    'unary : primary'
    p[0] = p[1]


def p_primary_id(p):
    'primary : ID'
    p[0] = env.get(p[1])

def p_primary(p):
    """primary : NUMBER
               | BOOLEAN
               | LPAREN expression RPAREN
               | STRING"""

    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 2:
        p[0] = p[1]



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


if __name__ == '__main__':




    # Build the parser
    parser = yacc.yacc()

    while True:
       try:
           s = input('expression : ')
       except EOFError:
           break
       if not s: continue
       result = parser.parse(s)
       print("env : ",env.values)