#-*- coding: utf-8 -*-
''' contient toutes les fonctions qu'on peut appliquer sur des sequents pour en obtenir d'autres
    les arguments passes sont dans la liste l et doivent des propositions ou des entiers '''
from mathplus import *

def print_sequent(s) :
	lp,p = s
	hypo = ', '.join([str(prop) for prop in lp])
	return hypo + ' |- ' + str(p)

def new(sequents, l = []) :
	""" cree un sequent vide """
	sequents.append(([], Node("True", [])))

def addhyp(sequents, l) :
	""" ajoute une proposition ( list[1] ) dans la liste des hypotheses du sequent n° list[0] """
	print l
	i = int(l[2])
	p = l[4]
	sequents[i][0].append(p)

def axiomintro(sequents, l) :
	''' passe l'hypothese numéro l[0] du séquent numero l[1] en conclusion du sequent '''
	try : 
		a = int(l[2])
		b = int(l[4])
	except ValueError:
		print "les arguments d'axiomintro ne sont pas des nombres"
	lp, p = sequents[b]
	sequents[b] = lp, lp[a]

def andintro(sequents, l):
	""" fait l'union des deux conclusion de deux sequents """
	(lp,p),(lpb,pb) = sequents[int(l[2])], sequents[int(l[4])]
	if lp == lpb:
		sequents.append((lp, Node("and", [p, pb])))
	else :
		print "fuck"


matchInstruction = {
	"new" : new,
	"addhyp" : addhyp,
	"axiomintro" : axiomintro,
	"andintro": andintro
	}

	
