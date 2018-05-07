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



def acg():
    #num_type = 1
    forest = []
    terms = ["bague", "chamai", "matalii"]

    forest = first_three(forest, terms)
    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest 

def ain():
    #num_type = 4
    forest = []
    terms = ["sine", "tu", "re", "ine", "asikne"]
    
    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 6)
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

    forest = mem_set(forest, ["tu", "re", "ine", "asikne"])
    forest = mem_set(forest, ["sine", "tu", "re", "ine", "asikne", "iwan", "arwan", "tupesan", "sinepesan"])
    forest = mem_set(forest, ["wan", "hotne", "wan e tu hotne", "tu hotne", "wan e re hotne", "re hotne", "wan e ine hotne",
                     "ine hotne", "wan e asikne hotne"])
    return forest


def ana():
    #num_type = 1
    forest = []
    terms = ["peada", "betacata", "quimisha"]

    forest = first_three(forest, terms)

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

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(make_tree(terms[4], [6, 100], "HIG"))

    return forest

def bae():
    #num_type = 1
    forest = []
    terms = ["baku-nakaji", "biku-nama", "kijiku-nama"]

    forest = first_three(forest, terms)

    forest.append(make_tree(terms[2], [4, 100], "HIG"))

    return forest

def eng():
    #num_type = 6
    forest = []
    terms = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 12)
    forest.append(make_tree(["w", "teen"], ["w", "ten"], "ADD"))
    forest.append(make_tree(["u", "ty"], ["u", "ten"], "MUL"))
    forest.append(make_tree(["u", "ty", "v"], ["u", "ten", "v"], "MTA"))
    forest.append(make_tree("hundred", ["ten", "two"], "POW"))
    forest = mem_set(forest, ["thir", "four", "fif", "six", "seven", "eigh", "nine", "twen", "thir", "for", "fif", "six", "seven", "eigh", "nine", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
    forest.append(make_tree("twen", "two", "EQU"))
    forest.append(make_tree("thir", "three", "EQU"))
    forest.append(make_tree("for", "four", "EQU"))
    forest.append(make_tree("fif", "five", "EQU"))
    forest.append(make_tree("eigh", "eight", "EQU"))

    return forest

def geo():
    #num_type = 5
    forest = []
    terms = ["ert-i", "or-i", "sam-i", "otx-i", "xut-i", "ekvs-i", "svid-i", "rva", "cxra", "at-i"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 10)
    forest.append(make_tree(["ca", "-", "met", "-i"], ["w", "at-i"], "ADD"))
    forest.append(make_tree(["cvid", "-", "met", "-i"], ["svid-i", "at-i"], "ADD"))
    forest.append(make_tree(["cxra", "-", "met", "-i"], ["cxra", "at-i"], "ADD"))
    forest.append(make_tree("oc-i", ["or-i", "at-i"], "MUL"))
    forest.append(make_tree(["v", "da", "-", "u"], ["v", "u"], "ADD"))
    forest.append(make_tree("as-i", ["at-i", "or-i"], "POW"))
    forest = mem_set(forest, ["ert -i", "or -i", "otx -i", "xut -i", "ekvs -i", "vra -i"])
    forest = mem_set(forest, ["oc-", "or-m-oc", "sam-oc-", "otx-m-oc"])
    forest = mem_set(forest, ["1-[digit for brevity]", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"
                              , "14", "15", "16", "17", "18", "19"])

    return forest



def goo():
    #num_type = 0
    forest = []
    terms = ["yoowarni", "garndiwiddidi", "ngarloodoo", "marla", "many"]

    for c in range(2):
	forest.append(make_tree(terms[c], c+1, "ONE"))

    for c in range(2, 4):
        forest.append(make_tree(terms[c], c+1, "GAU"))

    forest.append(make_tree(terms[4], [6, 100], "HIG"))

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

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 4)
    forest.append(make_tree(["cap", "cob", "popog"], ["?aedapuh", "?ayup"], "ADD"))
    forest.append(make_tree(["u", "cob", "cakget"], ["?u", "?aedapuh"], "ADD"))
    forest.append(make_tree(["cob", "ni-", "hu?"], ["?aedapuh", "ko?ap"], "MUL"))
    forest.append(make_tree(["v", "jib", "cakget"], ["v", "cob ni-hu?"], "ADD"))
    forest.append(make_tree(["?ayup", "jib", "hu?"], ["?aedapuh", "mora?ap"], "MUL"))
    forest.append(make_tree(["jib", "ni-", "hu?"], ["?aedapuh", "babni"], "MUL"))
    forest.append(make_tree("jib ni-hu?", [21, 100], "HIG"))
    forest = mem_set(forest, ["ko?ap", "mora?ap", "babni", "form(another)", "ko?ap", "mora?ap", "babni"])
    forest.append(make_tree("form(another", "?ayup", "EQU")) 

    return forest


def imo():
    #num_type = 1
    forest = []
    terms = ["mugasl", "sabla", "sabla mugo", "sabla sabla", "sabla sabla mugo"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
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


def mnd():
    #num_type = 6
    forest = []
    terms = ["yil", "er4", "san1", "si4", "wu3", "liu4", "qil", "ba1", "jiu3", "shi2"]
    
    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 9)
    forest.append(make_tree(["w", "shi2"], ["w", "shi2"], "MUL"))
    forest.append(make_tree(["u", "v"], ["u", "v"], "ADD"))
    forest.append(make_tree("bai3", ["shi2", "er4"], "POW"))

    forest = mem_set(["er4", "san1", "si4", "wu3", "liu4", "qi1", "ba1", "jiu3", "shi2", "er4shi2", "san1shi2", "si4shi2", "wu3shi2", "liu4shi2", "qi1shi2", "ba1shi2", "jiu3shi2", "yi1", "er4", "san1", "si4", "wu3", "liu4", "qi1", "ba1", "jiu3"]) 
    
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


def prh():
    #num_type = 0
    forest = []
    
    forest.append(make_tree("hoi_1", 1, "GAU"))
    forest.append(make_tree("hoi_2", [2, 4], "GAU"))
    forest.append(make_tree("aibaagi", [5, 100], "GAU"))

    return forest


def ram():
    #num_type = 1
    forest = []
    terms = ["saimig", "puksak", "pansak", "kugkugbi", "kwikistar"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(make_tree(terms[4], [6, 100], "HIG"))

    return forest

def war():
    forest = []
    
    forest.append(make_tree("xica pe", 1, "ONE"))
    forest.append(make_tree("dois", 2, "GAU"))
    forest.append(make_tree("many", [3, 100], "GAU"))
 
    return forest

def wsk():
    #num_type = 1
    forest = []
    terms = ["itoketa", "itelala", "iteltoke"]

    forest = first_three(forest, terms)
    
    forest.append(make_tree(["w", "-", "w"], ["w", "w"], "ADD"))
    forest.append(make_tree(["w-w", "itoketa"], ["w", "w", "itoketa"], "ADD"))
    forest.append(make_tree(["iteltoke", "-", "iteltoke", "-", "itelala"], ["iteltoke-iteltoke", "itelala"], "ADD"))
    forest.append(make_tree(["kuting", "dilisan", "sa", "itelala", "-", "itelala"], ["itelala-itelala-itoketa", "itelala-itelala"], "ADD"))
    forest.append(make_tree(["kuting", "dilisan", "-", "dilisan"], ["itelala-itelala-itoketa", "itelala"], "MUL"))
    forest.append(make_tree("kuting dilisan-dilisan", [11, 100], "HIG"))
    forest = mem_set(forest, ["itelala", "iteltoke"])

    return forest

def wch():
    #num_type = 1
    forest = []
    terms = ["wenyala", "tagw", "najtefwayal", "fwantes ihi", "qwe wenyal", "ipofwustoj", "ipofwusfwaya el", "ipofwusfwantes ihi", "oqwecho taqs"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 9)
    forest.append(make_tree(terms[8], [11, 100], "HIG"))

    return forest

def yid():
    #num_type = 1
    forest = []
    terms = ["guman", "jambul", "dagul", "yunggan gunyjii", "mala"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)

    return forest


def xoo():
    #num_type = 1
    forest = []
    terms = ["?ua(p)", "num(p)", "ae(p)"]

    forest = first_three(forest, terms)

    forest.append(make_tree(terms[2], [4, 100], "HIG"))
  
    return forest



# helper functions for common language aspects

def first_three(forest, terms):
    for c in range(3):
        forest.append(make_tree(terms[c], c+1, "ONE"))
         
    return forest

def successors(forest, terms, start, end):
	for c in range(start, end):
		forest.append(make_tree(terms[c], c+1, "SUC"))

	return forest

def mem_set(forest, term_list):
	for term in term_list:
		forest.append(make_tree(term, term, "MEM"))

	return forest

if __name__ == "__main__":
    f = mrt()
    forest_disp(f, "mrt")			 
