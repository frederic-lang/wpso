#-*- coding: utf-8 -*-

def enum(**enums):
    return type('Enum', (), enums)
Type = enum(UNDEFINED = 0, PROP = 1, TERM = 2, BOUNDTERM = 3, VAR = 4)


# symbol["symbol_name"] = ( symbol_sort, ( tuple of its arguments sort ) , symbol_syntax_code )
""" symbol syntax code :
	1 -> op x
	2 -> op x y
	3 -> x op y
	4 -> op x, y  """
	
symbol = {}
symbol["forall"] = ( Type.PROP, (Type.BOUNDTERM, Type.PROP), 2 )
symbol["exists"] = ( Type.PROP, (Type.BOUNDTERM, Type.PROP), 2 )
symbol["implies"] = ( Type.PROP, (Type.PROP, Type.PROP), 4 )
symbol["or"] = ( Type.PROP, (Type.PROP, Type.PROP), 4 )
symbol["and"] = ( Type.PROP, (Type.PROP, Type.PROP), 4 )
symbol["not"] = ( Type.PROP, (Type.PROP,), 1 )
symbol["plus"] = ( Type.TERM, (Type.TERM, Type.TERM), 4 )
symbol["equals"] = ( Type.PROP, (Type.TERM, Type.TERM), 4 )
symbol["S"] = ( Type.TERM, (Type.TERM,), 1 )


# Constants of the language are recorded in a dictionnary, its keys are constants' names and its items are their sort
constant = { "True" : Type.PROP, "False" : Type.PROP }


""" formatting symbol fonctions according to their ( i = syntax code, name = symbol_name, arg = symbol_children_list """

syntax = [
	lambda name : name , 
	lambda name, arg : name + " " + arg,
	lambda name, a, b : name + " "+ a + ", " + b,
	lambda name, a, b : name + " "+ a + " " + b,
	lambda name, a, b : a + " " + name + " " + b,
	]
