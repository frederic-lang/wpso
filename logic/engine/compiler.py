#-*- coding: utf-8 -*-
from mathplus.Node import Node
from mathplus.Sequent import Sequent
from parser import yacc_parse
import sys, traceback
from django.contrib.auth.models import User

class Compiler(object) :
	def __init__(self, text = "", is_superuser = False) :
		self.text = text
		self.sequents = [Sequent()]
		self.printed = []
		self.error = "no error"
		self.is_superuser = is_superuser
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
			exc_type, exc_value, exc_traceback = sys.exc_info()
			lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
			self.error = lines
			return False 
	def getSequentsPrinted(self):
		self.printed = range(len(self.sequents))
		for j in range(len(self.sequents)) :
			self.printed[j] = "Sequent " + str(j) + " : " + str(self.sequents[j])
		return self.printed
	def getConclusion(self) :
		return str(self.sequents[-1].conclusion)
	def getConclusionNode(self) :
		return self.sequents[-1].conclusion
	def getError(self) :
		return self.error
	def setText(self, t = ""):
		self.text = t
	def getText(self):
		return self.text
	def couldBeFinished(self):
		if self.is_superuser:
			return True
		else :
			return len( self.sequents[-1].hyp) == 0

if __name__ == "__main__" :
	print "votre demo est vraie : "
	import sys
	prog = file(sys.argv[1]).read()
	c = Compiler(prog)
	print c.compileSucessfully()
	print c.getSequentsPrinted()
		
