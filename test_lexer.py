
from verboze_lexer import lexer

# Test it out
data = '''
if 1 then display "toto";
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

