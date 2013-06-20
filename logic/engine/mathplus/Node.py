#-*- coding: utf-8 -*-
"""define the Node object which constitute the base of Trees, which represent Propositions"""
from data.peanoLanguage import *

def matchType(uptype, children) :
	if uptype == Type.PROP:
		if not( children.type == Type.PROP ) :
			raise Exception(str(children) + " should be of sort PROP, but is of sort " + strtype(children.type))
	if uptype == Type.TERM:
		if not( children.type == Type.TERM or children.type == Type.VAR ):
			raise Exception(str(children) + " should be of sort TERM, but is of sort " + strtype(children.type))
	if uptype == Type.BOUNDVAR:
		if not( children.type == Type.VAR) :
			raise Exception(str(children) + " should be a variable, but is of sort " + strtype(children.type))
			
			
			
class Node(object) :
	def __init__(self, name = "True", children = []) :
		self.name = name
		self.children =  list([c.copy() for c in children])
		if symbol.has_key(self.name) :
			self.type = symbol[self.name][0]
			self.syntaxCode = symbol[self.name][2]
			n = len(self.children)
			if n == len(symbol[self.name][1]) :
				for i in range(n) :
					matchType(symbol[self.name][1][i], self.children[i])
			else :
				raise Exception(str(self.name) + " hasn't the number of arguments it should have ")
		elif constant.has_key(self.name) :
			self.type = constant[self.name]
			self.syntaxCode = 0
			if len(self.children) != 0 :
				raise Exception("a constant cannot have arguments")
		elif type(self.name) == int :
			self.type = Type.TERM
			self.syntaxCode = 0
		else :
			self.type = Type.VAR
			self.syntaxCode = 0
			if len(self.children) != 0 :
				raise Exception("a variable cannot have arguments")
			
	def substitute(self, x, y) :
		""" replace Node x by Node y in the Tree built over self """
		def match(e) :
			if e == x :
				return y
			else :
				if isinstance(e, Node) :
					e.substitute(x, y)
				return e
		self.children = map(match, self.children)	
	def __str__(self) :
		return syntax[self.syntaxCode](str(self.name), *[ str(c) for c in self.children ])
	def __eq__(self, o) :
		return self.name == o.name and self.children == o.children
	def copy(self) :
		return Node(self.name, self.children)
	def isVar(self,x) : 
		for c in self.children :
			if c.isVar(x) :
				return True
		return x.name == self.name
	def isFreeVar(self, x) :
		if not(x.type == Type.VAR) :
			raise Exception(str(x) + " should be of type VAR")
		if self.name == 'forall' or self.name == 'exists' :
			[ v, p] = self.children
			if v == x :
				return False
			return p.isFreeVar(x)
		else :
			for c in self.children :
				if c.isFreeVar(x) :
					return True
			return x.name == self.name
				
