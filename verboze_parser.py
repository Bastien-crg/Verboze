import ply.yacc as yacc
from verboze_lex import tokens


def p_expression_logical_or(p):
    'expression : logical_or'
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

def p_primary_boolean(p):
    'primary : BOOLEAN'
    p[0] = p[1]

def p_primary_expr(p):
    'primary : LPAREN expression RPAREN'
    p[0] = p[2]

def p_primary_num(p):
    'primary : NUMBER'
    p[0] = p[1]



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('expression : ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)