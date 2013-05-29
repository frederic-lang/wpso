#-*- coding: utf-8 -*-
import ply.lex as lex

tokens = (
'NUMBER',
'WORD',
'COMMA',
'QUANTIFIER',
'OPERATOR',
'NOT',
'INSTRUCTION',
'SPACE',
'RPAREN',
'LPAREN',
'SEMICOLON',
'DOLLAR'
)

t_COMMA = r','
t_QUANTIFIER = r'forall|exists'
t_OPERATOR = r'include|implies|belongs|and|or'
t_WORD = r'\w+'
t_INSTRUCTION = r'new|addhyp|trueintro|axiomintro|falseelim|andintro|left|right|orintroright|orintroleft|orelim|impliesintro|implieselim|notintro|notelim|forallintro|forallelim|existsintro|existselim|excludedmiddle'
t_NOT = r'ceciestunenegation|not'
t_RPAREN = r'\)'
t_LPAREN = r'\('
t_SEMICOLON = r';'
t_DOLLAR = r'\$'


def t_NUMBER(t) :
	r'\d+'
	t.value = int(t.value)
	return t
	
t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error ( t ) :
	raise Exception(' Lexer : Illegal character, code ASCII : ' + str(ord(t.value[0])) )
	t.lexer.skip(1)

lex.lex()

print "Le lexer a été lexé"

if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	lex.input( prog )
	while 1:
		tok = lex.token()
		if not tok : break
		print " line %d : %s (%s)" %(tok.lineno, tok.type, tok.value )






