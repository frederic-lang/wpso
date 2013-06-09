#-*- coding: utf-8 -*-
from Node import Node

					
class Sequent(object) :
	def __init__(self, hyp = [], conclusion = Node("True")) :
		self.hyp = list(hyp)
		self.conclusion = conclusion.copy()
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
