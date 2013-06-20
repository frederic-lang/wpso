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
	i = i.name
	s = sequents[i].copy()
	hyp = s.hyp
	c = s.conclusion
	for p in hyp :
		if p.isFreeVar(x) :
			raise Exception(" forallintro is forbidden because " + str(x) + " shouldn't be a free variable of " + str(p))	
	sequents.append(Sequent(hyp, Node("forall", [x, c])))
	

def forallelim(sequents, i, v) :
	i = i.name
	s = sequents[i].copy()
	if s.conclusion.name == "forall" :
		[x, q] = s.conclusion.children
		q.substitute(x, v)
		s.conclusion = q
		sequents.append(s)
		
		
def existsintro(sequents, i, v, x) :
	i = i.name
	s = sequents[i].copy()
	s.conclusion.substitute(v, x)
	s.conclusion = Node("exists", [x, s.conclusion])
	sequents.append(s)

def existselim(sequents, i, j) :
	i = i.name
	j = j.name
	sa = sequents[i].copy()
	sb = sequents[j].copy()
	if sa.conclusion.name == "exists" :
		[x, a] = sa.conclusion.children
		if a in sb.hyp and sb.hyp.remove(a) == sa.hyp :
			for p in sa.hyp : 
				if p.isFreeVar(x) :
					raise Exception(" existselim is forbidden because " + str(x) + " shouldn't be a free variable of " + str(p))
				if sb.conclusion.isFreeVar(x) :
					raise Exception(" existselim is forbidden because " + str(x) + " shouldn't be a free variable of " + str(sb.conclusion))
				
			sequents.append(Sequent(sa.hyp, sb.conclusion))
		else : 
			raise Exception( str(sb) + " and " + str(sa) + " should have same hypothesis." 

def excludedmiddle(sequents, i, p) :
	i = i.name
	hyp = sequents[i].copy().hyp
	sequents.append(Sequent(hyp, Node("or", [p, Node("not", [p])])))

def induction(sequents, i, j) :
	i = i.name
	j = j.name
	s = sequents[i]
	t = sequents[j]
	if not(s.hyp == t.hyp) :
		raise Exception("sequent "+ str(i) + " and sequent " + str(j) + " should have same hypothesis")
	if t.conclusion.name == "forall" :
		k = t.conclusion.children[0]
		imp = t.conclusion.children[1]
		kplus1 = Node("S", [ Node("k", []) ])
		if imp.name == "implies" :
			p = imp.children[0].copy()
			q = imp.children[1].copy()
			q.substitute(kplus1, k)
			if q == p :
				q.substitute(k, Node(0, []))
				if q == s.conclusion:
					sequents.append(Sequent(s.hyp, Node("forall", [k, p])))
				else :
					raise Exception(" sequent " + str(i) + " should have for conclusion " + str(q))
			else :
				raise Exception( str(q) + " and " + str(p) + " should be equals ")
		else :
			raise Exception(" sequent " + str(j) + " should have a conclusion matching with 'forall k, P(k) implies P(S k)'")
	else:
		raise Exception("sequent " +str(j) + " should begin with 'forall' ")
			
			
def rewrite(sequents, i, j) :
	i = i.name
	j = j.name
	s = sequents[i]
	t = sequents[j]
	if s.hyp == t.hyp :
		eq = s.conclusion.copy()
		p = t.conclusion.copy()
		if eq.name == "equals" :
			[a,b] = s.conclusion.children
			p.substitute(a,b)
			sequents.append(Sequent(s.hyp, p))
		else :
			raise Exception(str(eq) + "should be an equality")
	else :
		raise Exception("sequent "+ str(i) + " and sequent " + str(j) + " should have same hypothesis")

def rewritinv(sequents, i, j) :
	i = i.name
	j = j.name
	s = sequents[i]
	t = sequents[j]
	if s.hyp == t.hyp :
		eq = s.conclusion.copy()
		p = t.conclusion.copy()
		if eq.name == "equals" :
			[a,b] = s.conclusion.children
			p.substitute(b,a)
			sequents.append(Sequent(s.hyp, p))
		else :
			raise Exception(str(eq) + "should be an equality")
	else :
		raise Exception("sequent "+ str(i) + " and sequent " + str(j) + " should have same hypothesis")


def shiftequality(sequents, i):
	i = i.name
	s = sequents[i].copy()
	eq = s.conclusion
	if eq.name == "equals" :
		[a,b] = eq.children
		a = Node("S", [a])
		b = Node("S", [b])
		eq.children = [a,b]
		sequents.append(Sequent(s.hyp, eq))
		
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
	"excludedmiddle" : excludedmiddle,
	"induction" : induction,
	"rewrite" : rewrite,
	"rewritinv" : rewritinv,
	"shiftequality" : shiftequality,
	}


if __name__ == "__main__" :
	import sys
	prog = file(sys.argv[1]).read()
	result = parser.parse( prog, tracking=True )
	print "et on a :"
	print result

