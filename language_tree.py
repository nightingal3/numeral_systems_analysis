from anytree import Node, RenderTree, LevelOrderIter
from anytree.dotexport import RenderTreeGraph
from anytree.exporter import DotExporter
import os
from langstrategy import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def make_tree(form, numexp, op):
	"""Makes a tree for the given expression, where the left subtree represents the form and the right subtree represents the expression."""
	root = Node("=")
	
	#construct the tree according to the setting given. 
	if op == "ONE" or op == "EQV":
	    if op == "EQV":
		root = Node(u'\u2263')
	    l = Node(form, parent=root)
	    r = Node(numexp, parent=root)
	    
	elif op == "GAU":
		l = Node(form, parent=root)
		r_root = Node("g", parent=root)
		r_exp = Node(numexp, parent=r_root)

	elif op == "SUC":
		l = Node(form, parent=root)
		r_root = Node("s", parent=root)
		r_exp = Node(numexp - 1, parent=r_root)
			
	elif op == "HIG":			  	
	    l = Node(form, parent=root)
	    r = Node("...", parent=root)	
	    r_l = Node(str(numexp[0]), parent=r)
	    r_r = Node(str(numexp[1]), parent=r)
	
	elif op in ["ADD", "SUB", "MUL", "DIV", "POW"]:
            l_root = Node(form[0], parent=root)
            l_c = Node(form[1], parent=l_root)
	    if op == "ADD":
                r_root = Node("+", parent=root)
	    elif op == "SUB":
		r_root = Node("-", parent=root)
	    elif op == "MUL":
		r_root = Node(u'\u2715'.encode("utf-8"), parent=root)
	    elif op == "DIV":
		r_root = Node(u'\u00f7', parent=root)
	    elif op == "POW":
		r_root = Node(u'\u2191', parent=root)
            r_l_root = Node("m", parent=r_root)
            r_r_root = Node("m", parent=r_root)
            r_l_c = Node(numexp[0], parent=r_l_root)
            r_r_c = Node(numexp[1], parent=r_r_root)
        	

	elif op == "MTA" or op == "MTS":
	    l_root = Node(form[2], parent=root)
            l_l_0 = Node(form[0], parent=l_root)
            l_l_1 = Node(form[1], parent=l_l_0)
            l_r = Node(form[3], parent=l_root)

            r_root = Node("+", parent=root)
            r_l_r = Node(u'\u2715'.encode("utf-8"), parent=r_root)
            r_l_l = Node("m", parent=r_l_r)
            r_l_l_1 = Node(numexp[0], parent=r_l_l)
            r_l_r = Node("m", parent=r_l_r)
            r_l_r_1 = Node(numexp[1], parent=r_l_r)
            r_r = Node("m", parent=r_root)
            r_r_1 = Node(numexp[2], parent=r_r)        
    
	return root

def build_language(langcode, prnt=False):
	f = open(os.getcwd() + "/complexities/langlist.txt", "r+") 	
	langcodes = f.read().split('\r\n')
	f.close()

	if langcode not in langcodes:
            print("Please enter a valid language code (see complexities/langcodes.txt)")
	    return
	
	strat_res = eval(langcode)()
  	
	if prnt:
	    forest_disp(strat_res, langcode)
	#strategy.calc_complexity()
	#strategy.print_grammar()
	return 

def calc_complexity_base(tree):
	"""Calculates the complexity (defined by number of nodes)"""
	return len([node for node in LevelOrderIter(tree)])


def disp(tree, filename=None):
	if filename:
	   RenderTreeGraph(tree).to_picture(os.path.abspath(filename + ".png"))
	return RenderTree(tree)

def forest_disp(forest, langcode):
	if not os.path.exists(langcode):
	    os.makedirs(langcode)
	for i, tree in enumerate(forest, 1):
	   print("dfsf")
	   disp(tree, langcode + "/" +  str(i))
	return 	

if __name__ == "__main__":
	f = make_tree("sdf", [3, 20], "HIG")
	print(disp(f, "hig"))
	assert False
	t = make_tree("one", 1, "ONE")
	t1 = make_tree(["u", "ty"], ["u", 10], "MUL")
	t2 = make_tree("four", 4, "SUC")
        t3 = make_tree(["w", "teen"], ["w", 10], "ADD")
	t4 = make_tree("twen", 2, "EQV")
        t5 = make_tree(["twen", "ty", "-", "one"], [2, 10, 1], "MTA")
	print(disp(t))
	print(disp(t1, "eng_xty"))
	print(disp(t2, "eng_four"))
        print(disp(t3, "eng_teen"))
        print(disp(t5, "eng_mta"))
	#print(disp(t4, "eng_eqv"))
        print(calc_complexity_base(t3))
	print(calc_complexity_base(t2))
