import language_tree
import pickle
import os
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
#might use for cleaniness, might not
class Language:
	def __init__(self, num_type, ulim, num_only=False, date=None):
		self.num_type = num_type
		self.ulim = ulim
		self.forest = []
                self.num_only = num_only
		self.date = date

	def get_num_type(self):
		return self.num_type
	
	def get_ulim(self):
		return self.ulim

	def get_forest(self):
		return self.forest

	def get_date(self):
		return self.date

	def add_rule(self, form, numeral, op):
		self.forest.append(language_tree.make_tree(form, numeral, op, self.num_only))
                              
        def first_three(self, terms):
                for c in range(3):
                        self.forest.append(language_tree.make_tree(terms[c], c+1, "ONE", self.num_only))

	def subitize_gen(self, terms):
		for c in range(len(terms)):
			self.forest.append(language_tree.make_tree(terms[c], c+1, "ONE", self.num_only))

        def successors(self, start, end, terms=None):
		if terms is None:
			terms = [i for i in range(end)]
                for c in range(start, end):
                        self.forest.append(language_tree.make_tree(terms[c], c+1, "SUC", self.num_only))

            
def acg():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["bague", "chamai", "matalii"]

    forest = first_three(forest, terms)
    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))

    return forest, num_type, ulim 

def ain():
    num_type = 4
    ulim = None
    forest = []
    terms = ["sine", "tu", "re", "ine", "asikne"]
    
    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    #10
    forest.append(language_tree.make_tree("wan", ["tu", "asikne"], "MUL")) 	
    #6-9
    forest.append(language_tree.make_tree(["i", "wan"], ["wan", "ine"], "SUB"))
    forest.append(language_tree.make_tree(["ar", "wan"], ["wan", "re"], "SUB"))
    forest.append(language_tree.make_tree(["tu", "pesan"], ["wan", "tu"], "SUB"))
    forest.append(language_tree.make_tree(["sine", "pesan"], ["wan", "sine"], "SUB"))
    #20
    forest.append(language_tree.make_tree("hotne", ["tu", "wan"], "MUL"))
    forest.append(language_tree.make_tree(["wan", "e", "w", "hotne"], ["w", "hotne", "wan"], "MTS"))
    forest.append(language_tree.make_tree(["w", "hotne"], ["w", "hotne"], "MUL"))
    forest.append(language_tree.make_tree(["v", "ikasma", "u"], ["v", "u"], "ADD"))

    forest.append(language_tree.make_tree("u", ["tu", "re", "ine", "asikne"], "MEM"))
    forest.append(language_tree.make_tree("v", ["sine", "tu", "re", "ine", "asikne", "iwan", "arwan", "tupesan", "sinepesan"], "MEM"))
    forest.append(language_tree.make_tree("w", ["wan", "hotne", "wan e tu hotne", "tu hotne", "wan e re hotne", "re hotne", "wan e ine hotne",
                     "ine hotne", "wan e asikne hotne"], "MEM"))
    return forest, num_type, ulim


def ana():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["peada", "betacata", "quimisha"]

    forest = first_three(forest, terms)

    forest.append(language_tree.make_tree(["quimsha", "beta"], [4, 100], "HIG"))

    return forest, num_type, ulim


def awp():
    num_type = 1
    ulim = 4
    forest = []
    terms = ["maza", "pas", "kutna", "ambara"]

    forest = first_three(forest, terms)
 
    forest.append(language_tree.make_tree("ambara", 4, "SUC"))
    forest.append(language_tree.make_tree("ambara", [5, 100], "HIG"))

    return forest, num_type, ulim

def brs():
    num_type = 1
    ulim = 5
    forest = []
    terms = ["sig-u/o", "hua-ra", "idia-ra", "babarirak-u/o", "kohobokarak-u/o"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(language_tree.make_tree(terms[4], [6, 100], "HIG"))

    return forest, num_type, ulim

def bae():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["baku-nakaji", "biku-nama", "kijiku-nama"]

    forest = first_three(forest, terms)

    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))

    return forest, num_type, ulim

def eng():
    num_type = 6
    ulim = None
    forest = []
    terms = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 12)
    forest.append(language_tree.make_tree(["w", "teen"], ["w", "ten"], "ADD"))
    forest.append(language_tree.make_tree(["u", "ty"], ["u", "ten"], "MUL"))
    forest.append(language_tree.make_tree(["u", "-", "ty", "v"], ["u", "ten", "v"], "MTA"))
    forest.append(language_tree.make_tree("hundred", ["ten", "two"], "POW"))
    forest.append(language_tree.make_tree("u", ["thir", "four", "fif", "six", "seven", "eigh", "nine"], "MEM"))
    forest.append(language_tree.make_tree("v", ["twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"], "MEM"))
    forest.append(language_tree.make_tree("w", ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], "MEM"))
    forest.append(language_tree.make_tree("twen", "two", "EQU"))
    forest.append(language_tree.make_tree("thir", "three", "EQU"))
    forest.append(language_tree.make_tree("for", "four", "EQU"))
    forest.append(language_tree.make_tree("fif", "five", "EQU"))
    forest.append(language_tree.make_tree("eigh", "eight", "EQU"))

    return forest, num_type, ulim

def geo():
    num_type = 5
    ulim = None
    forest = []
    terms = ["ert-i", "or-i", "sam-i", "otx-i", "xut-i", "ekvs-i", "svid-i", "rva", "cxra", "at-i"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 10)
    forest.append(language_tree.make_tree(["t", "-", "w", "met"], ["w", "at-i"], "ADD"))
    forest.append(language_tree.make_tree(["ca", "-", "met", "-i"], ["sam-i", "at-i"], "ADD"))
    forest.append(language_tree.make_tree(["cvid", "-", "met", "-i"], ["svid-i", "at-i"], "ADD"))
    forest.append(language_tree.make_tree(["cxra", "-", "met", "-i"], ["cxra", "at-i"], "ADD"))
    forest.append(language_tree.make_tree("oc-i", ["or-i", "at-i"], "MUL"))
    forest.append(language_tree.make_tree(["or", "-", "m", "-", "oc-i"], ["or-i", "oc-i"], "MUL"))
    forest.append(language_tree.make_tree(["sam", "-", "oc-i"], ["sam-i", "oc-i"], "MUL"))
    forest.append(language_tree.make_tree(["otx", "-", "m", "-", "oc-i"], ["otx-i", "oc-i"], "MUL"))
    forest.append(language_tree.make_tree(["v", "da", "-", "u"], ["v", "u"], "ADD"))
    forest.append(language_tree.make_tree("as-i", ["at-i", "or-i"], "POW"))
    forest.append(language_tree.make_tree("w", ["ert -i", "or -i", "otx -i", "xut -i", "ekvs -i", "vra -i"], "MEM"))
    forest.append(language_tree.make_tree("v", ["oc-", "or-m-oc", "sam-oc-", "otx-m-oc"], "MEM"))
    forest.append(language_tree.make_tree("u", ["1-[digit for brevity]", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"
                              , "14", "15", "16", "17", "18", "19"], "MEM"))

    return forest, num_type, ulim



def goo():
    num_type = 0
    ulim = None
    forest = []
    terms = ["yoowarni", "garndiwiddidi", "ngarloodoo", "marla", "many"]

    for c in range(2):
	forest.append(language_tree.make_tree(terms[c], c+1, "ONE"))

    for c in range(2, 4):
        forest.append(language_tree.make_tree(terms[c], c+1, "GAU"))

    forest.append(language_tree.make_tree(terms[4], 7, "GAU"))

    return forest, num_type, ulim


def hix():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["towenyxa", "asako", "osorwawo"]

    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))

    return forest, num_type, ulim

def hpd():
    num_type = 1
    ulim = 20
    forest = []
    terms = ["?ayup", "ko?ap", "mora?ap", "babni", "?aedapuh"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(language_tree.make_tree(["cap", "cob", "popog"], ["?aedapuh", "?ayup"], "ADD"))
    forest.append(language_tree.make_tree(["u", "cob", "cakget"], ["?u", "?aedapuh"], "ADD"))
    forest.append(language_tree.make_tree(["cob", "ni-", "hu?"], ["?aedapuh", "ko?ap"], "MUL"))
    forest.append(language_tree.make_tree(["v", "jib", "cakget"], ["v", "cob ni-hu?"], "ADD"))
    forest.append(language_tree.make_tree(["?ayup", "jib", "hu?"], ["?aedapuh", "mora?ap"], "MUL"))
    forest.append(language_tree.make_tree(["jib", "ni-", "hu?"], ["?aedapuh", "babni"], "MUL"))
    forest.append(language_tree.make_tree("jib ni-hu?", [21, 100], "HIG"))
    forest.append(language_tree.make_tree("u", ["ko?ap", "mora?ap", "babni"], "MEM"))
    forest.append(language_tree.make_tree("v",["form(another)", "ko?ap", "mora?ap", "babni"], "MEM"))
    forest.append(language_tree.make_tree("form(another", "?ayup", "EQU")) 

    return forest, num_type, ulim


def imo():
    num_type = 1
    ulim = 5
    forest = []
    terms = ["mugasl", "sabla", "sabla mugo", "sabla sabla", "sabla sabla mugo"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(language_tree.make_tree(terms[4], [6, 100], "HIG"))

    return forest, num_type, ulim

def kay():
    num_type = 1
    ulim = 4
    forest = []
    terms = ["warngiida", "kiyarrngka", "burldamurra", "mirdinda", "muthaa"]

    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(terms[3], 4, "SUC"))
    forest.append(language_tree.make_tree(terms[4], [5, 100], "HIG"))

    return forest, num_type, ulim


def mnd():
    num_type = 6
    ulim = None
    forest = []
    terms = ["yil", "er4", "san1", "si4", "wu3", "liu4", "qil", "ba1", "jiu3", "shi2"]
    
    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 10)
    forest.append(language_tree.make_tree(["w", "shi2"], ["w", "shi2"], "MUL"))
    forest.append(language_tree.make_tree(["u", "v"], ["u", "v"], "ADD"))
    forest.append(language_tree.make_tree("bai3", ["shi2", "er4"], "POW"))

    forest.append(language_tree.make_tree("u", ["er4", "san1", "si4", "wu3", "liu4", "qi1", "ba1", "jiu3"], "MEM"))
    forest.append(language_tree.make_tree("v", ["shi2", "er4shi2", "san1shi2", "si4shi2", "wu3shi2", "liu4shi2", "qi1shi2", "ba1shi2", "jiu3shi2"], "MEM"))
    forest.append(language_tree.make_tree("w", ["yi1", "er4", "san1", "si4", "wu3", "liu4", "qi1", "ba1", "jiu3"], "MEM"))
    
    return forest, num_type, ulim	

    
def myi():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["yawumbawa", "yabaranwa", "yabalawa"]
    
    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))

    return forest, num_type, ulim

def mrt():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["kalika", "kayarra", "jarrkurti", "maruwarla"]

    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(terms[3], [4, 100], "HIG"))

    return forest, num_type, ulim


def pit():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["kutju", "kutjara", "mankurpa"]
    
    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))

    return forest, num_type, ulim


def prh():
    num_type = 0
    ulim = None
    forest = []
    
    forest.append(language_tree.make_tree("hoi_1", 1, "GAU"))
    forest.append(language_tree.make_tree("hoi_2", [2, 4], "GAU"))
    forest.append(language_tree.make_tree("aibaagi", [5, 100], "GAU"))

    return forest, num_type, ulim


def ram():
    num_type = 1
    ulim = 5
    forest = []
    terms = ["saimig", "puksak", "pansak", "kugkugbi", "kwikistar"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(language_tree.make_tree(terms[4], [6, 100], "HIG"))

    return forest, num_type, ulim


def war():
    num_type = 0
    ulim = None
    forest = []
    
    forest.append(language_tree.make_tree("xica pe", 1, "ONE"))
    forest.append(language_tree.make_tree("dois", 2, "GAU"))
    forest.append(language_tree.make_tree("many", [3, 100], "GAU"))
 
    return forest, num_type, ulim

def wch():
    num_type = 1
    ulim = 10
    forest = []
    terms = ["wenyala", "tagw", "najtefwayal", "fwantes ihi", "qwe wenyal", "ipofwuj", "ipofwustoj", "ipofwusfwaya el", "ipofwusfwantes ihi", "oqwecho taqs"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 10)
    forest.append(language_tree.make_tree(terms[8], [11, 100], "HIG"))

    return forest, num_type, ulim


def wsk():
    num_type = 1
    ulim = 10
    forest = []
    terms = ["itoketa", "itelala", "iteltoke"]

    forest = first_three(forest, terms)
    
    forest.append(language_tree.make_tree(["w", "-", "w"], ["w", "w"], "ADD"))
    forest.append(language_tree.make_tree(["w", "-", "w", "itoketa"], ["w-w", "itoketa"], "ADD"))
    forest.append(language_tree.make_tree(["iteltoke", "-", "iteltoke", "-", "itelala"], ["iteltoke-iteltoke", "itelala"], "ADD"))
    forest.append(language_tree.make_tree(["kuting", "dilisan", "sa", "itelala", "-", "itelala"], ["itelala-itelala-itoketa", "itelala-itelala"], "ADD"))
    forest.append(language_tree.make_tree(["kuting", "dilisan", "-", "dilisan"], ["itelala-itelala-itoketa", "itelala"], "MUL"))
    forest.append(language_tree.make_tree("kuting dilisan-dilisan", [11, 100], "HIG"))
    forest.append(language_tree.make_tree("u", ["itelala", "iteltoke"], "MEM"))

    return forest, num_type, ulim

def yid():
    num_type = 1
    ulim = 5
    forest = []
    terms = ["guman", "jambul", "dagul", "yunggan gunyjii", "mala"]

    forest = first_three(forest, terms)
    forest = successors(forest, terms, 3, 5)
    forest.append(language_tree.make_tree("mala", [6, 100], "HIG"))
    return forest, num_type, ulim


def xoo():
    num_type = 1
    ulim = 3
    forest = []
    terms = ["?ua(p)", "num(p)", "ae(p)"]

    forest = first_three(forest, terms)

    forest.append(language_tree.make_tree(terms[2], [4, 100], "HIG"))
  
    return forest, num_type, ulim



# helper functions for common language aspects

def first_three(forest, terms, num_only=False):
    for c in range(3):
        forest.append(language_tree.make_tree(terms[c], c+1, "ONE", num_only))
         
    return forest

def successors(forest, terms, start, end):
	for c in range(start, end):
		forest.append(language_tree.make_tree(terms[c], c+1, "SUC"))

	return forest

if __name__ == "__main__":
    #all_langs = dir(langstrategy)
    #f = mrt()
    #forest_disp(f, "mrt")
                                  
    #Old Irish
    sga = Language(6, None, num_only=True, date=750)
    sga.first_three([1, 2, 3]) 
    sga.successors(4, 10)
    sga.add_rule(None, ["u", 10], "ADD")
    sga.add_rule(None,  ["u", 20, "v"], "MTA")
    sga.add_rule(None, ["u", "base"], "MUL")
    sga.add_rule(None, ["u", 10, "v"], "MTA")
    sga.add_rule(None, [10, 2], "POW")
    if not os.path.exists("language_objects"):
	os.makedirs("language_objects")
    pickle.dump(sga, open("language_objects/sga.p", "w"))
   
    #Ainu
    ain = Language(4, None, num_only=False)
    ain.first_three(["sine", "tu", "re", "ine", "asikne"])

    
