#-*- coding: utf-8 -*-
"""define the Node object which constitute the base of Trees, which represent Propositions"""

def enum(**enums):
    return type('Enum', (), enums)
Type = enum(UNDEFINED = 0, PROP = 1, TERM = 2)


opData = {}
opData["forall"] = ( Type.PROP, (Type.TERM, Type.PROP) )
opData["exists"] = ( Type.PROP, (Type.TERM, Type.PROP) )
opData["include"] = ( Type.PROP, (Type.TERM, Type.TERM) )
opData["implies"] = ( Type.PROP, (Type.PROP, Type.PROP) )
opData["belongs"] = ( Type.PROP, (Type.TERM, Type.TERM) )
opData["or"] = ( Type.PROP, (Type.PROP, Type.PROP) )
opData["and"] = ( Type.PROP, (Type.PROP, Type.PROP) )
opData["not"] = ( Type.PROP, (Type.PROP,) )
opData["True"] = ( Type.PROP,)
opData["False"] = ( Type.PROP,)

class Node(object) :
	def __init__(self, name, children = []) :
		self.name = name
		self.children = list(children)
		self.type = Type.UNDEFINED
		self.type = opData[self.name][0]
	def substitute(self, x, y) :
		def match(e) :
			if e == x :
				return y
			else :
				if isinstance(e, Node) :
					e.substitute(x, y)
				return e
		self.children = map(match, self.children)	
	def __str__(self) :
		if self.name == "include" or self.name == "belongs" or self.name == "implies" or self.name == "and" or self.name == "or":
			text = str(self.children[0]) + " "+ self.name + " " + str(self.children[1])
		elif self.name == "forall" or self.name == "exists":
			a = self.children[0]
			b = self.children[1]
			text = self.name + " " + str(a) + ", " + str(b)
		elif self.name == "not" :
			text = self.name + " " + str(self.children[0])
		else :
			text = self.name
		return text
	def __eq__(self, o) :
		return self.name == o.name and self.children == o.children
	def copy(self) :
		return Node(self.name, self.children)
