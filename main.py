from verboze_lex import lexer

# Test it out
data = '''
is greater than 
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

