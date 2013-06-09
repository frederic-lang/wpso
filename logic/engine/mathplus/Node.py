#-*- coding: utf-8 -*-
"""define the Node object which constitute the base of Trees, which represent Propositions"""
from data.peanoLanguage import *

class Node(object) :
	def __init__(self, name = "True", children = []) :
		self.name = name
		self.children =  list(children)
		if symbol.has_key(self.name) :
			self.type = symbol[self.name][0]
			self.syntaxCode = symbol[self.name][2]
		elif constant.has_key(self.name) :
			self.type = constant[self.name]
			self.syntaxCode = 0
		else :
			self.type = Type.VAR
			self.syntaxCode = 0
	def substitute(self, x, y) :
		""" replace Node x by Node y in the Tree build over self """
		def match(e) :
			if e == x :
				return y
			else :
				if isinstance(e, Node) :
					e.substitute(x, y)
				return e
		self.children = map(match, self.children)	
	def __str__(self) :
		return syntax[self.syntaxCode](self.name, *[ str(c) for c in self.children ])
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
		if self.name == 'forall' or self.name == 'exists' :
			[ v, p] = self.children
			if v.name == x.name :
				return False
			return p.isFreeVar(x)
		else :
			for c in self.children :
				if c.isFreeVar(x) :
					return True
			return x.name == v.name
				
