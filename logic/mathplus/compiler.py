#-*- coding: utf-8 -*-
from Node import Node
from Sequent import Sequent
from parser import *
from lexer import *

class Compiler(object) :
	def __init__(self, text = "") :
		self.text = text
		self.sequents = [Sequent()]
		self.printed = []
		self.error = "no error"
	def compileSuccessfully(self) :
		try :
			r = yacc_parse(self.text)
			instructions = r[1]
			self.sequents = [Sequent()]
			
			for i in instructions :
				f=i[0]
				args=i[1]
				f(self.sequents, *args)
			return True
		except Exception as e :
			self.error = str(e)
			return False 
	def getSequentsPrinted(self):
		self.printed = range(len(self.sequents))
		for j in range(len(self.sequents)) :
			self.printed[j] = "Séquent " + str(j) + " : " + str(self.sequents[j])
		return self.printed
	def getConclusion(self) :
		return str(self.sequents[-1].conclusion)
	def getError(self) :
		return self.error
	def setText(self, t = ""):
		self.text = t
	def getText(self):
		return self.text
	def couldBeFinished(self):
		return len( self.sequents[-1].hyp) == 0

if __name__ == "__main__" :
	print "heyhey compiler"
		
