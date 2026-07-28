
from verboze_lexer import lexer

# Test it out
data = '''
1 is greater than 0;
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

