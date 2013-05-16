#-*- coding: utf-8 -*-
from Node import Node
from mException import *

class Sequent(object) :
	def __init__(self, hyp = [], conclusion = Node("True")) :
		if type(hyp) == list and type(conclusion) == Node :
			self.hyp = list(hyp)
			self.conclusion = conclusion.copy()
		else :
			raise mException("Les hypotheses ('{0}') et la conclusion ('{1}') ne permettent pas de former un séquent".format(hyp, conclusion))
	def __str__(self) :
		hypo = ', '.join([str(prop) for prop in self.hyp])
		return 'gamma, ' + hypo + ' |- ' + str(self.conclusion)
	def copy(self) :
		return Sequent( list(self.hyp), self.conclusion.copy() )

if __name__ == "__main__" :
	try :
		sa = Sequent(3,Node("belongs", ["1", "2"]))
		print sa
	except mException as e:
		print e
		print type(e)
