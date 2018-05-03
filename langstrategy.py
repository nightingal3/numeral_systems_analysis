from language_tree import *

def abk():
    num_type = 5
    forest = []
    terms = ["gri", "at", "mumek", "mumat", "mufit", "munggwo", "musi", "musyu"]
    term_iter = 0
			
    for c in range(101):
        if c == 1:
	    forest.append(make_tree("dik", 1, "ONE"))
        elif c == 2:
	    forest.append(make_tree("we", 2, "ONE"))
	elif c == 3:
	    forest.append(make_tree("gre", 3, "ONE"))
	if c in range(4, 11):
	    forest.append(make_tree(terms[term_iter], c, "SUC"))
	    term_iter += 1

    return forest


if __name__ == "__main__":
    f = abk()
    forest_disp(f, "abk")			 
