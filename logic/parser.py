#-*- coding: utf-8 -*-
from mathplus import *
import ply.yacc as yacc
from lexer import tokens
from engine import matchInstruction

sequents = []

def print_sequent(s) :
	lp,p = s
	hypo = ', '.join([str(prop) for prop in lp])
	return 'gamma, ' + hypo + ' |- ' + str(p)

def p_explist(p):
    '''explist :
    | explist instr'''
    if(len(p) < 3):
        p[0] = ('EXPLIST', [])
    else:
        p[1][1].append(p[2])
        p[0] = p[1]


def p_instr_def0(p) :
	'''instr : INSTRUCTION NEWLINE
	          | INSTRUCTION RPAREN expression LPAREN NEWLINE
	          | INSTRUCTION RPAREN expression DOLLAR expression LPAREN NEWLINE'''
	f = matchInstruction[p[1]]
	f(sequents, p[1:])
	p[0] = p[1:]

def p_expression_word(p):
	'expression : WORD'
	p[0] = p[1]

def p_expression_quantifier(p):
	''' expression : QUANTIFIER expression COMMA expression '''
	p[0] = Node( p[1], [ p[2], p[4] ] )
	
def p_expression_op(p):
	''' expression : expression OPERATOR expression'''
	p[0] = Node( p[2], [ p[1], p[3] ] )

def p_expression_not(p):
	'''expression : NOT expression '''
	p[0] = Node( "not", [p[1]] )

def p_error(e ):
    print("error : %s" %e )
    yacc.errok()



def yacc_parse(text) :
	r = yacc.parse(text, tracking=True)
	return [ print_sequent(s) for s in sequents ]
	
yacc.yacc ( outputdir = 'generated' )
if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	result = yacc.parse( prog, tracking=True )
	print "et on a :"
	for s in sequents :
		print '\t' + print_sequent(s)
	print result



