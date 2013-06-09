#-*- coding: utf-8 -*-
import ply.yacc as yacc
from lexer import tokens
from mathplus.Node import Node
from calculus import matchInstruction

def p_explist(p):
    '''explist :
    | explist instr'''
    if(len(p) < 3):
        p[0] = ('EXPLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]


def p_instr(p) :
	'''instr : INSTRUCTION args SEMICOLON'''
	f = matchInstruction[p[1]]
	p[0] = (f,p[2])

def p_args(p) :
	'''args : LPAREN RPAREN
		| LPAREN expression RPAREN
		| LPAREN expression COMMA expression RPAREN 
		| LPAREN expression COMMA expression COMMA expression RPAREN '''
	if len(p) == 3 :
		p[0] = []
	if len(p) == 4 :
		p[0] = [p[2]]
	if len(p) == 6 :
		p[0] = [p[2], p[4]]
	if len(p) == 8 :
		p[0] = [p[2], p[4], p[6]]

def p_expression_wordornumber(p):
	'''expression : WORD
	 	      | NUMBER '''
	p[0] = Node(p[1],[])

def p_expression_quantifier(p):
	''' expression : QUANTIFIER expression COMMA expression '''
	p[0] = Node( p[1], [ p[2], p[4] ] )
	
def p_expression_op(p):
	''' expression : expression OPERATOR expression'''
	p[0] = Node( p[2], [ p[1], p[3] ] )

def p_expression_not(p):
	'''expression : NOT expression '''
	p[0] = Node( "not", [p[2]] )

def p_expression_group(t):
	'''expression : LPAREN expression RPAREN'''
	t[0] = t[2]
	
def p_error(e ):
	raise Exception("error : %s" %e )
	yacc.errok()


precedence = (
    ('nonassoc', 'INSTRUCTION'),  # Nonassociative operators
    ('nonassoc', 'QUANTIFIER', 'COMMA'),
    ('left', 'OPERATOR'),
    ('right', 'NOT')
    )
    
parser = yacc.yacc()

def yacc_parse(text) :
	r = parser.parse(text, tracking=True)
	return r
	
if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	result = parser.parse( prog, tracking=True )
	print "et on a :"
	print result



