
from verboze_lex import lexer

# Test it out
data = '''
variable a worth 2; variable b worth 3;
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

