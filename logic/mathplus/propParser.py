#-*- coding: utf-8 -*-
import ply.yacc as yacc
from lexer import tokens
from Node import Node
from Sequent import Sequent


def p_expression_wordornumber(p):
	'''expression : WORD
	 	      | NUMBER '''
	p[0] = p[1]

def p_expression_quantifier(p):
	''' expression : QUANTIFIER expression COMMA expression '''
	p[0] = Node( p[1], [ p[2], p[4] ] )
	
def p_expression_op(p):
	''' expression : expression OPERATOR expression'''
	p[0] = Node( p[2], [ p[1], p[3] ] )

def p_expression_not(p):
	'''expression : NOT expression '''
	p[0] = Node( "not", [p[2]] )
	
def p_error(e ):
	raise Exception("error : %s" %e )
	yacc.errok()


precedence = (
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
	print result, type(result)

