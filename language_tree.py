from anytree import Node, RenderTree, LevelOrderIter
from anytree.dotexport import RenderTreeGraph
import os

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
	
	elif op == "ADD" or op == "SUB":
            l_root = Node(form[0], parent=root)
            l_c = Node(form[1], parent=l_root)
	    if op == "ADD":
                r_root = Node("+", parent=root)
	    else:
		r_root = Node("-", parent=root)
            r_l_root = Node("m", parent=r_root)
            r_r_root = Node("m", parent=r_root)
            r_l_c = Node(numexp[0], parent=r_l_root)
            r_r_c = Node(numexp[1], parent=r_r_root)
        	
	elif op == "POW":
	    raise NotImplementedError 

	return root


def calc_complexity(tree):
	"""Calculates the complexity (defined by number of nodes)"""
	return len([node for node in LevelOrderIter(tree)])


def disp(tree, filename=None):
	if filename:
	   print(os.path.abspath(filename + ".png"))
	   print(os.path.exists(os.path.abspath(filename + ".png")))
	   RenderTreeGraph(tree).to_picture(os.path.abspath(filename + ".png"))
	return RenderTree(tree)
	

if __name__ == "__main__":
	t = make_tree("one", 1, "ONE")
	t1 = make_tree("hoi_1", 1, "GAU")
	t2 = make_tree("four", 4, "SUC")
        t3 = make_tree(["w", "teen"], ["w", 10], "ADD")
	t4 = make_tree("twen", 2, "EQV")
	print(disp(t))
	print(disp(t1))
	print(disp(t2, "eng_four"))
        print(disp(t3, "eng_teen"))
	print(disp(t4, "eng_eqv"))
        print(calc_complexity(t3))
	print(calc_complexity(t2))
