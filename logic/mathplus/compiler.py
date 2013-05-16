#-*- coding: utf-8 -*-
from Node import Node
from Sequent import Sequent
from parser import *
from lexer import *

	
def make(text) :
	try :
		r = yacc_parse(text)
		instructions = r[1]
		sequents = []
		for i in instructions :
			f=i[0]
			args=i[1]
			f(sequents, *args)
		return [str(s) for s in sequents]
	except IndexError as e :
		return [ "tu as probablement appelé un numéro de sequent ou de proposition qui n'existe pas", str(e) ]
	except Exception as e :
		return [ "erreur : " + str(e) ]
	
	
if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	seq = make(prog)
	for s in seq :
		print s
		
