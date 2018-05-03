from anytree import Node, RenderTree, LevelOrderIter
from anytree.dotexport import RenderTreeGraph
from anytree.exporter import DotExporter
import os
import langstrategy


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
		raise NotImplementedError
	
	elif (op == "ADD" or op == "SUB") or (op == "MUL" or op == "DIV"):
            l_root = Node(form[0], parent=root)
            l_c = Node(form[1], parent=l_root)
	    if op == "ADD":
                r_root = Node("+", parent=root)
	    elif op == "SUB":
		r_root = Node("-", parent=root)
	    elif op == "MUL":
		r_root = Node(u'\u2715', parent=root)
	    elif op == "DIV":
		r_root = Node(u'\u00f7', parent=root)
            r_l_root = Node("m", parent=r_root)
            r_r_root = Node("m", parent=r_root)
            r_l_c = Node("numexp[0]", parent=r_l_root)
            r_r_c = Node("numexp[1]", parent=r_r_root)
        	

	elif op == "POW":
	    raise NotImplementedError

	return root

def build_language(langcode, prnt=False):
	f = open(os.getcwd() + "/complexities/langlist.txt", "r+") 	
	langcodes = f.read().split('\r\n')
	f.close()

	if langcode not in langcodes:
        print("Please enter a valid language code (see complexities/langcodes.txt)")
		return
	
	strategy = langstrategy.langcode()
	strategy.calc_complexity()
	strategy.print_grammar()
	return 

def calc_complexity_base(tree):
	"""Calculates the complexity (defined by number of nodes)"""
	return len([node for node in LevelOrderIter(tree)])


def disp(tree, filename=None):
	if filename:
	   RenderTreeGraph(tree).to_picture(os.path.abspath(filename + ".png"))
	return RenderTree(tree)
	

if __name__ == "__main__":
	build_language("xdl")
	t = make_tree("one", 1, "ONE")
	t1 = make_tree(["u", "ty"], ["u", 10], "MUL")
	t2 = make_tree("four", 4, "SUC")
        t3 = make_tree(["w", "teen"], ["w", 10], "ADD")
	t4 = make_tree("twen", 2, "EQV")
	print(disp(t))
	print(disp(t1, "eng_xty"))
	print(disp(t2, "eng_four"))
        print(disp(t3, "eng_teen"))
	#print(disp(t4, "eng_eqv"))
        print(calc_complexity_base(t3))
	print(calc_complexity_base(t2))
