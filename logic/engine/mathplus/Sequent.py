#-*- coding: utf-8 -*-
from Node import Node
from data.peanoLanguage import Type

					
class Sequent(object) :
	def __init__(self, hyp = [], conclusion = Node("True")) :
		self.hyp = list(hyp)
		for h in hyp:
			if not(h.type == Type.PROP) :
				raise Exception( str(h) + " should be of type PROP ")
		self.conclusion = conclusion.copy()
		if not( conclusion.type == Type.PROP) :
			raise Exception( str(conclusion) + " should be of type PROP")
	def __str__(self) :
		hypo = '; '.join([str(prop) for prop in self.hyp])
		return 'gamma; ' + hypo + ' |- ' + str(self.conclusion)
	def copy(self) :
		return Sequent( self.hyp, self.conclusion)




if __name__ == "__main__" :
	try :
		sa = Sequent([],Node("equals", ["1", "1"]))
		print sa
	except Exception as e:
		print e
		print type(e)
