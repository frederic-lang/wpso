

def enum(**enums):
    return type('Enum', (), enums)
Type = enum(PROP = 1, TERM = 2)

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
		self.children = children
		self.Type = hydrate(self.name)
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
		if self.name == "include" or self.name == "belongs" or self.name == "implies":
			text = str(self.children[0]) + " "+ self.name + " " + str(self.children[1])
		elif self.name == "forall" or self.name == "exists":
			a = self.children[0]
			b = self.children[1]
			text = self.name + " " + str(a) + ", " + str(b)
		else :
			text = self.name
		return text

def hydrate(name) :
	return opData[name][0]

	
def axiomintro(lp,p):
	if p in lp :
		return lp,p
		
def trueintro(lp):
	return lp, Node( "True", [])
	
def falseelim(seq,q):
	(lp,p) = seq
	if p.name == "false" :
		return lp,q

def andintro(seq, seqb):
	(lp,p),(lpb,pb) = seq, seqb
	if lp == lpb:
		return lp, Node("and", [p, pb])
	
def left(seq):
	(lp,p) = seq
	if p.name == "and" :
		(l, r) = p.children
		return lp, l
	return n

def right(seq):

	(lp,p) = seq
	if p.name == "and" :
		(l, r) = p.children
		return lp, r
	return n

def orintroright(seq, q) :
	(lp, p) = seq
	return lp, Node("or", [p, q])

def orintroleft(seq, q):
	(lp, p) = seq
	return lp, Node("or", [q, p])

def orelim(seqor, seqa, seqb):
	(lp,aorb) = seqor
	[a, b] = aorb.children
	(lpa, qa) = seqa
	(lpb, qb) = seqb
	if qa==qb and ( a in lpa) and ( b in lpb ) :
		if lpa.remove(a) == lpb.remove(b) : 
			lpa.append(a)
			lpa.append(b)
			return lp, qa

def impliesintro(seq, a):
	(lp, p) = seq
	if a in lp :
		lp.remove(a)
		return lp, Node("implies", [a, p])

def implieselim(seqimp, seqa) :
	(lp, aimpb) = seqimp
	(lp2, a) = seqa
	if aimpb.name == "implies" :
		[qa, b] = aimpb.children
		if qa==a and lp == lp2:
			return lp, b
			
def notintro(seq, a) :
	(lp, p) = seq
	if a in lp and p.name == "False" :
		return lp.remove(a), Node("not", [a])

def notelim(seq1, seq2) :
	(lp1, a) = seq1
	(lp2, nota) = seq2
	if lp1 == lp2 and nota.name == "not" :
		[a2] == nota.children
		if a2 == a :
			return lp1, Node("False", [])

def forallintro(seq, v) :
	lp, p = seq
	return lp,  Node("forall", [v, p])

def forallelim(seq, v) :
	lp, p = seq
	if p.name == "forall" :
		[x, q] = p.children
		q.substitute(x, v)
		return lp, q
		
def existsintro(seq, v, x) :
	lp, p = seq
	q = p.substitute(v, x)
	return lp, Node("exists", [x, q])

def existselim(seq1, seq2) :
	lp, exa = seq1
	lpa, b = seq2
	if exa.name == "exists" :
		[x, a] = exa.children
		if a in lpa and lpa.remove(a) == lp :
			return lp, b

def excludedmiddle(lp, a) :
	return lp, Node("or", [a, Node("not", [a])])


	
def apply(n,v) :
	if n.name == "forall" :
		(x, m) = n.children
		m.substitute(x, v)
		return m
	return n


