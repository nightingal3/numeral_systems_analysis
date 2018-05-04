from language_tree import *
"""
	num_type meaning:
	0: restricted approximate
	1: restricted exact
	2: body-part
	3: other base
	4: vigesimal
	5: hybrid
	6: decimal
"""



def abk(): 
    #num_type = 5
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

def acg():
    #num_type = 1
    forest = []
    terms = ["bague", "chamai", "matalii"]

    for c in range(3):
	forest.append(make_tree(terms[c], c-1, "ONE"))
    
    forest.append(make_tree(terms[3], [4, 100], "HIG"))

    return forest 

def ain():
    #num_type = 4
    forest = []
    terms0 = ["sine", "tu", "re", "ine", "asikne"]
    
    for c in range(3):
	forest.append(make_tree(terms[c], c+1, "ONE"))

    for c in range(3, 6):
	forest.append(make_tree(terms[c], c+1, "SUC"))
    #10
    forest.append(make_tree("wan", ["tu", "asikne"], "MUL")) 	
    #6-9
    forest.append(make_tree(["i", "wan"], ["wan", "ine"], "SUB"))
    forest.append(make_tree(["ar", "wan"], ["wan", "re"], "SUB"))
    forest.append(make_tree(["tu", "pesan"], ["wan", "tu"], "SUB"))
    forest.append(make_tree(["sine", "pesan"], ["wan", "sine"], "SUB"))
    #20
    forest.append(make_tree("hotne", ["tu", "wan"], "MUL"))
    
    for c in range(30, 100, 20):
	forest.append(make_tree(["wan", "e", "w", "hotne"], ["w", "hotne", "wan"], "MULSUB"))

    for c in range(40, 120, 20):
	forest.append(make_tree(["w", "hotne"], ["w", "hotne"], "MUL"))

    for c in range(11, 110, 11):
	forest.append(make_tree(["v", "ikasma", "u"], ["v", "u"], "ADD"))

    #?
    return forest


def ana():
    #num_type = 1
    forest = []
    terms = ["peada", "betacata", "quimisha"]

    for c in range(3):
	forest.append(make_tree(terms[c], c+1, "ONE"))

    forest.append(make_tree(["quimsha", "beta"], [4, 100], "HIG"))

    return forest


def awp():
    #num_type = 1
    forest = []
    terms = ["maza", "pas", "kutna", "ambara"]

    forest = first_three(forest, terms)
 
    forest.append(make_tree("ambara", 4, "SUC"))
    forest.append(make_tree("ambara", [5, 100], "HIG"))

    return forest

def brs():
    #num_type = 1
    forest = []
    terms = ["sig-u/o", "hua-ra", "idia-ra", "babarirak-u/o", "kohobokarak-u/o"]

    for c in range(6):
	if c in range(3):
	    forest.append(make_tree(terms[c], c+1, "ONE"))
	else:
	    forest.append(make_tree(terms[c], c+1, "SUC"))

    forest.append(make_tree(terms[4], [6, 100], "HIG"))

    return forest

def bae():
    #num_type = 1
    forest = []
    terms = ["baku-nakaji", "biku-nama", "kijiku-nama"]

    forest = first_three(forest, terms)

    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest

def hix():
    #num_type = 1
    forest = []
    terms = ["towenyxa", "asako", "osorwawo"]

    forest = first_three(forest, terms)
    
    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest

def hpd():
    #num_type = 1
    forest = []
    terms = ["?ayup", "ko?ap", "mora?ap", "babni" "?aedapuh"]

    return forest


def imo():
    #num_type = 1
    forest = []
    terms = ["mugasl", "sabla", "sabla mugo", "sabla sabla", "sabla sabla mugo"]

    forest = first_three(forest, terms)
    
    for c in range(3, 5):
        forest.append(make_tree(terms[c], c+1, "SUC"))

    forest.append(make_tree(terms[4], [6, 100], "HIG"))

    return forest

def kay():
    #num_type = 1
    forest = []
    terms = ["warngiida", "kiyarrngka", "burldamurra", "mirdinda", "muthaa"]

    forest = first_three(forest, terms)
    
    forest.append(make_tree(terms[3], 4, "SUC"))
    forest.append(make_tree(terms[4], [5, 100], "HIG"))

    return forest
    
def myi():
    #num_type = 1
    forest = []
    terms = ["yawumbawa", "yabaranwa", "yabalawa"]
    
    forest = first_three(forest, terms)
    
    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest

def mrt():
    #num_type = 1
    forest = []
    terms = ["kalika", "kayarra", "jarrkurti", "maruwarla"]

    forest = first_three(forest, terms)
    
    forest.append(make_tree(terms[3], [4, 100], "HIG"))

    return forest


def pit():
    #num_type = 1
    forest = []
    terms = ["kutju", "kutjara", "mankurpa"]
    
    forest = first_three(forest, terms)
    
    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest


def ram():
    #num_type = 1
    forest = []
    terms = ["saimig", "puksak", "pansak", "kugkugbi", "kwikistar"]

    forest = first_three(forest, terms)
    
    for c in range(3, 5):
        forest.append(make_tree(terms[c], c+1, "SUC")) 
    
    forest.append(make_tree(terms[4], [6, 100], "HIG"))

    return forest

def wsk():
    #num_type = 1
    forest = []
    terms = ["itoketa", "itelala", "iteltoke"]

    forest = first_three(forest, terms)
    
    forest.append(make_tree(["w", "-", "w"], ["w", "w"], "ADD"))
    forest.append(make_tree(["w-w", "itoketa"], ["w", "w", "itoketa"], "ADD"))
    #TODO: make multi-add func

    forest.append(make_tree("kuting dilisan-dilisan", [11, 100], "HIG"))
    return forest

def wch():
    #num_type = 1
    forest = []
    terms = ["wenyala", "tagw", "najtefwayal", "fwantes ihi", "qwe wenyal", "ipofwustoj", "ipofwusfwaya el", "ipofwusfwantes ihi", "oqwecho taqs"]

    forest = first_three(forest, terms)

    for c in range(3, 9):
	forest.append(make_tree(terms[c], c+1, "SUC"))

    forest.append(make_tree(terms[8], [11, 100], "HIG"))

    return forest

def yid():
    #num_type = 1
    forest = []
    terms = ["guman", "jambul", "dagul", "yunggan gunyjii", "mala"]

    forest = first_three(forest, terms)
    
    for c in range(3, 5):
        forest.append(make_tree(terms[c], c+1, "SUC"))

    return forest


def xoo():
    #num_type = 1
    forest = []
    terms = ["?ua(p)". "num(p)", "ae(p)"]

    forest = first_three(forest, terms)

    forest.append(make_tree(terms[2], [4, 100], "HIG"))
  
    return forest



# helper functions for common language aspects

def first_three(forest, terms):
    for c in range(3):
        forest.append(make_tree(terms[c], c+1, "ONE"))
         
    return forest


if __name__ == "__main__":
    f = mrt()
    forest_disp(f, "mrt")			 
