import ply.lex as lex

tokens = (
'WORD',
'COMMA',
'QUANTIFIER',
'OPERATOR',
'NOT',
'INSTRUCTION',
'NEWLINE',
'RPAREN',
'LPAREN',
'DOLLAR'
)

t_COMMA = r','
t_QUANTIFIER = r'forall|exists'
t_OPERATOR = r'include|implies|belongs|and|or'
t_NOT = r'not'
t_WORD = r'\w+'
t_INSTRUCTION = r'new|addhyp|axiomintro|andintro'
t_RPAREN = r'\('
t_LPAREN = r'\)'
t_DOLLAR = r'\$'


def t_NEWLINE( t ) :
	r'\n+'
	t.lexer.lineno += len( t.value )
	return t

t_ignore = '[ \t]'

def t_error ( t ) :
	print "Illegal character '%s' " % t.value[0]
	t.lexer.skip(1)

lex.lex()

print "heyhey : start"

if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	lex.input( prog )
	while 1:
		tok = lex.token()
		if not tok : break
		print " line %d : %s (%s)" %(tok.lineno, tok.type, tok.value )






