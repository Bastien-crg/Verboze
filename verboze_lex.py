import ply.lex as lex


# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'BOOLEAN',
    'NOT',          # !
    'LT',           # <
    'GT',           # >
    'LTE',          # <=
    'GTE',          # >=
    'EQUAL',        # ==
    'NE',           # !=
    'AND',          # &
    'OR'            # |

)

# Regular expression rules
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NOT     = r'\ not\ '
t_LT      = r'\ is\ lower\ than\ '
t_GT      = r'\ is\ greater\ than\ '
t_LTE     = r'\ is\ lower\ or\ equal\ to\ '
t_GTE     = r'\ is\ greater\ or\ equal\ to\ '
t_EQUAL   = r'\ is\ equal\ to\ '
t_NE      = r'\ is\ not\ equal\ to\ '
t_AND     = r'\ and\ '
t_OR      = r'\ or\ '

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_BOOLEAN(t):
    r'true|false'
    return t.value == 'true'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
# t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'is' : 'IS',
    'not' : 'NOT',
    'lower' : 'LOWER',
    'than' : 'THAN',
    'and' : 'AND',
    'or' : 'OR',
    'equal' : 'EQUAL',
    'to' : 'TO',
    'greater' : 'GREATER'

}

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     t.type = reserved.get(t.value,'ID')    # Check for reserved words
#     return t

# Build the lexer
lexer = lex.lex()





