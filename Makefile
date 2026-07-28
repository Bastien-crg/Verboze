verboze: lex.l parser.y
	bison -d parser.y
	flex lex.l
	gcc -o $@ parser.tab.c lex.yy.c -lfl
