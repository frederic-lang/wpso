#-*- coding: utf-8 -*-
""" contains all of the basic operations which make sequents from sequents.
    Each function has for arguments "sequents", which is the list of sequents to manipulate, and "l", which is the list of indications"""
from mathplus.Sequent import Sequent
from mathplus.Node import Node
from library.models import Demonstration
import pickle


def new(sequents) :
	""" create a empty sequent """
	sequents.append(Sequent([], Node("True", [])))

def addhyp(sequents, i, p) :
	i = i.name
	sequents.append(sequents[i].copy())
	sequents[-1].hyp.append(p)

def trueintro(sequents, i):
	i = i.name
	sequents[i].conclusion = Node( "True", [])
	
def axiomintro(sequents, a,b) :
	a = a.name
	b = b.name
	s = Sequent(sequents[b].hyp, sequents[b].hyp[a])
	sequents.append(s)

def lemmaintro(sequents, n) :
	n = n.name
	lemma = Demonstration.objects.get(id = n)
	c = pickle.loads(str(lemma.lemmaNode))
	sequents.append(Sequent([], c))

def falseelim(sequents, i, p):
	i = i.name
	s = sequents[i].copy()
	if s.conclusion.name == "False" :
		s.conclusion = p
		sequents.append(s)
	
def andintro(sequents, i,j):
	i = i.name
	j = j.name
	seqa, seqb = sequents[i], sequents[j]
	if seqa.hyp == seqb.hyp :
		sequents.append( Sequent(seqa.hyp, Node("and", [seqa.conclusion, seqb.conclusion])))
	else :
		raise Exception("Sequents don't have same hypothesis in this andintro")
	
def left(sequents, i):
	i = i.name
	s = sequents[i].copy()
	if s.conclusion.name == "and" :
		s.conclusion = s.conclusion.children[0]
		sequents.append(s)

def right(sequents, i):
	i = i.name
	s = sequents[i].copy()
	if s.conclusion.name == "and" :
		s.conclusion = s.conclusion.children[1]
		sequents.append(s)

def orintroright(sequents, i, q) :
	sequents[i].conclusion = Node("or", [sequents[i].conclusion, q])

def orintroleft(sequents, i, q) :
	i = i.name
	sequents[i].conclusion = Node("or", [q,sequents[i].conclusion])

def orelim(sequents, i, j, k): # à améliorer
	i = i.name
	j = j.name
	k = k.name
	seqor = sequents[i]
	seqa = sequents[j]
	seqb = sequents[k]
	if seqor.conclusion.name == "or" :
		[a, b] = seqor.conclusion.children
	else :
		raise Exception("Sequent " + str(i) + " hasn't a 'or' conclusion")
	if not(seqa.conclusion == seqb.conclusion) :
		raise Exception("Sequent j and k haven't the same conclusion")
	else :
		if not( a in seqa.hyp) :
			raise Exception(" proposition " + str(a) + "doesn't belong to sequent "+ str(j) +"'s hypothesis") 
		if not( b in seqb.hyp ):
			raise Exception(" proposition " + str(a) + "doesn't belong to sequent "+ str(k) +"'s hypothesis") 
		if seqa.hyp.remove(a) == seqb.hyp.remove(b) : 
			seqa.hyp.append(a)
			sequents.append(Sequent(seqb.hyp, seqb.conclusion))
			seqb.hyp.append(b)

def impliesintro(sequents, i, j):
	i = i.name
	j = j.name
	s = sequents[j].copy()
	h = s.hyp[i]
	s.hyp.remove(h)
	s.conclusion = Node("implies", [h, s.conclusion])
	sequents.append(s)

def implieselim(sequents, i, j) :
	i = i.name
	j = j.name
	aimpb = sequents[j].copy()
	a = sequents[i].copy()
	if aimpb.conclusion.name == "implies" :
		[ha, b] = aimpb.conclusion.children
		if ha==a.conclusion and a.hyp == aimpb.hyp:
			sequents.append(Sequent(a.hyp, b))
			
def notintro(sequents, i, j) :
	i = i.name
	j = j.name
	s = sequents[i]
	p = s.hyp[j]
	if s.conclusion.name == "False" :
		s.hyp.remove(p)
		sequents.append(Sequent(s, Node("not", [p])))
		s.hyp.append(p)

def notelim(sequents, i, j) :
	i = i.name
	j = j.name
	if sequents[i].hyp == sequents[j].hyp and sequents[j].conclusion.name == "not" :
		[p] = sequents[j].conclusion.children
		if p == sequents[i].conclusion :
			sequents.append(Sequent(sequents[j].hyp, Node("False", [])))

def forallintro(sequents, i, x) :
	"""à améliorer"""
	i = i.name
	hyp = sequents[i].hyp
	c = sequents[i].conclusion
	sequents.append(Sequent(hyp, Node("forall", [x, c])))

def forallelim(sequents, i, v) :
	i = i.name
	s = sequents[i]
	if s.conclusion.name == "forall" :
		[x, q] = s.conclusion.children
		q.substitute(x, v)
		s.conclusion = q
		
# une des 2 fn ci dessous à améliorer
		
def existsintro(sequents, i, v, x) :
	i = i.name
	s = sequents[i].copy()
	s.conclusion.substitute(v, x)
	s.conclusion = Node("exists", [x, s.conclusion])
	sequents.append(s)

def existselim(sequents, i, j) :
	i = i.name
	j = j.name
	sa = sequents[i]
	sb = sequents[j]
	if sa.conclusion.name == "exists" :
		[x, a] = sa.conclusion.children
		if a in sb.hyp and sb.hyp.remove(a) == sa.hyp :
			pass

def excludedmiddle(sequents, i, p) :
	i = i.name
	hyp = sequents[i].copy().hyp
	sequents.append(Sequent(hyp, Node("or", [p, Node("not", [p])])))




matchInstruction = {
	"new" : new,
	"addhyp" : addhyp,
	"trueintro" : trueintro,
	"axiomintro" : axiomintro,
	"lemmaintro" : lemmaintro,
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


if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	result = parser.parse( prog, tracking=True )
	print "et on a :"
	print result

