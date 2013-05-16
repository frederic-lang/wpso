#-*- coding: utf-8 -*-
""" contains all of the basic operations which make sequents from sequents.
    Each function has for arguments "sequents", which is the list of sequents to manipulate, and "l", which is the list of indications"""
from mException import *
from Sequent import Sequent
from Node import Node

def new(sequents) :
	""" create a empty sequent """
	sequents.append(Sequent([], Node("True", [])))

def addhyp(sequents, i, p) :
	sequents[i].hyp.append(p)

def trueintro(sequents, i):
	sequents[i].conclusion = Node( "True", [])
	
def axiomintro(sequents, a,b) :
	s = Sequent(sequents[b].hyp, sequents[b].hyp[a])
	sequents.append(s)

def falseelim(sequents, i, p):
	if sequents[i].conclusion.name == "False" :
		sequents[i].conclusion = p
	
def andintro(sequents, i,j):
	seqa, seqb = sequents[i], sequents[j]
	if seqa.hyp == seqb.hyp :
		sequents.append( Sequent(seqa.hyp, Node("and", [seqa.conclusion, seqb.conclusion])))
	else :
		raise mException("Sequents don't have same hypothesis in this andintro")
	
def left(sequents, i):
	if sequents[i].conclusion.name == "and" :
		sequents[i].conclusion = sequents[i].conclusion.children[0]

def right(sequents, i):
	if sequents[i].conclusion.name == "and" :
		sequents[i].conclusion = sequents[i].conclusion.children[1]

def orintroright(sequents, i, q) :
	sequents[i].conclusion = Node("or", [sequents[i].conclusion, q])

def orintroleft(sequents, i, q) :
	sequents[i].conclusion = Node("or", [q,sequents[i].conclusion])

def orelim(sequents, i, j, k): # à améliorer
	seqor = sequents[i]
	seqa = sequents[j]
	seqb = sequents[k]
	[a, b] = seqor.conclusion.children
	if seqa.conclusion == seqb.conclusion and ( a in seqa.hyp) and ( b in seqb.hyp ) and seqor.conclusion.name == "or":
		print "ca passe"
		if seqa.hyp.remove(a) == seqb.hyp.remove(b) : 
			print "ca repasse "
			seqa.hyp.append(a)
			sequents.append(Sequent(seqb.hyp, seqb.conclusion))
			seqb.hyp.append(b)

def impliesintro(sequents, i, j):
	s = sequents[i]
	h = s.hyp[j]
	s.hyp.remove(h)
	s.conclusion = Node("implies", [h, s.conclusion])

def implieselim(sequents, i, j) :
	aimpb = sequents[j]
	a = sequents[i]
	if aimpb.conclusion.name == "implies" :
		[ha, b] = aimpb.hyp.children
		if ha==a.conclusion and a.hyp == aimpb.hyp:
			sequents.append(Sequent(a.hyp, b))
			
def notintro(sequents, i, j) :
	s = sequents[i]
	p = s.hyp[j]
	if s.conclusion.name == "False" :
		s.hyp.remove(p)
		sequents.append(Sequent(s, Node("not", [p])))
		s.hyp.append(p)

def notelim(sequents, i, j) :
	if sequents[i].hyp == sequents[j].hyp and sequents[j].conclusion.name == "not" :
		[p] = sequents[j].conclusion.children
		if p == sequents[i].conclusion :
			sequents.append(Sequent(sequents[j].hyp, Node("False", [])))

def forallintro(sequents, i, x) :
	"""à améliorer"""
	hyp = sequents[i].hyp
	c = sequents[i].conclusion
	sequents.append(Sequent(hyp, Node("forall", [x, c])))

def forallelim(sequents, i, v) :
	s = sequents[i]
	if s.conclusion.name == "forall" :
		[x, q] = s.conclusion.children
		q.substitute(x, v)
		s.conclusion = q
		
# une des 2 fn ci dessous à améliorer
		
def existsintro(sequents, i, v, x) :
	s = sequents[i]
	s.conclusion.substitute(v, x)
	s.conclusion = Node("exists", [x, s.conclusion])

def existselim(sequents, i, j) :
	sa = sequents[i]
	sb = sequents[j]
	if sa.conclusion.name == "exists" :
		[x, a] = sa.conclusion.children
		if a in sb.hyp and sb.hyp.remove(a) == sa.hyp :
			pass

def excludedmiddle(sequents, i, p) :
	hyp = sequents[i].hyp
	sequents.append(Sequent(hyp, Node("or", [p, Node("not", [p])])))




matchInstruction = {
	"new" : new,
	"addhyp" : addhyp,
	"trueintro" : trueintro,
	"axiomintro" : axiomintro,
	"falseelim" : falseelim,
	"andintro": andintro,
	"left" : left,
	"right": right,
	"orintroright" : orintroright,
	"orintroleft" : orintroleft,
	"orelim" : orelim,
	"impliesintro" : impliesintro,
	"implieselim" : implieselim,
	"notintro" : notintro,
	"notelim" : notelim,
	"forallintro" : forallintro,
	"forallelim" : forallelim,
	"existsintro" : existsintro,
	"existselim" : existselim,
	"excludedmiddle" : excludedmiddle
	}

