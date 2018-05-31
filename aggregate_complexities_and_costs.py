import matplotlib
matplotlib.use("Agg")
import language_tree
import langstrategy
import inspect
from routines import compute_cost_size_principle, compute_cost
import numpy as np
import math
import matplotlib.pyplot as plt

def aggregate_complexities():
	info = {}
	
	#assume naming convention is respected...	
	langlist = [i[0] for i in inspect.getmembers(langstrategy, inspect.isfunction) if len(i[0]) == 3] 
	
	for i in range(len(langlist)):
		complexity, num_type, ulim = language_tree.build_language(langlist[i])
		info[langlist[i]] = (complexity, num_type)

	return info

def aggregate_communicative_costs(need_probs, lang_info):
	"""lang_info should be a dict organized as {lang:(comp, num_type)}
	* fix this mess later lol"""
	langs = lang_info.keys()
	complexities = [i[1][0] for i in lang_info.items()]
	lang_by_category = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
	term = {"prh": ["hoi_1", "hoi_2", "aibaagi"], "war": ["xica pe", "dois"], "goo": ["yoowarni", "garndiwiddidi", "ngarloodoo", "marla"]} #get rid of hardcoding here
	num_term_pt = {"prh":[1, 2, 2, 2, 3, 3, 3, 3, 3, 3], "war": [1, 2], "goo": [1, 2, 3, 3, 4]}
	end_category = {"prh": 0, "war": 1, "goo": 1}
	numberline = [i for i in range(1, 101)]
	for item in lang_info.items():
		lang_by_category[item[1][1]].append(item[0])	
	costs = {}
	ulim = {}

	#Restricted approximate systems
	for lang in lang_by_category[0]:
		print("lang")
		print(lang)
		print("mum_term_pt")
		print(num_term_pt[lang])
		print("end_category")
		print(end_category[lang])
		costs[lang] = compute_cost.compute_approx_cost(term[lang], numberline, num_term_pt[lang], end_category[lang], need_probs)
		print(costs[lang])	
			
	#Restricted exact systems	
	for lang in lang_by_category[1]:
		ulim[lang] = language_tree.build_language(lang)[2]
		costs[lang] = compute_cost_size_principle(ulim[lang], need_probs)

	ret = {}
	for lang in costs: #return as (complexity, cost, lang_type)
		ret[lang] = (lang_info[lang][0], costs[lang], lang_info[lang][1])	
	return ret

	
		
def plot_cost_vs_complexity(lang_info):
	colorscheme = {1: "green", 6: "blue", 0: "red"}
	print(lang_info)
	for lang in lang_info:	
		plt.plot([lang_info[lang][0]], [lang_info[lang][1]], label=lang, marker='o', color=colorscheme[lang_info[lang][2]], markersize=5)
	
	plt.xlabel("Complexity")
	plt.ylabel("Communicative cost")
	plt.savefig("cvc.png", dpi=1000)
	return	

if __name__ == "__main__":

	c = aggregate_complexities()
	f = open("data/need_probs/needprobs_eng_fit.csv")
	need_probs = [float(i) for i in f.read().split("\r\n")[:-1]]
	#print(need_probs)
	#print(c)
	x = aggregate_communicative_costs(need_probs, c)
	x["eng"] = (126, 0, 6)
	x["mnd"] = (92, 0, 6)
	x["geo"] = (167, 0, 6)
	x["ain"] = (121, 0, 6)
	print(x)
	plot_cost_vs_complexity(x)
	#print(aggregate_communicative_costs())

	
