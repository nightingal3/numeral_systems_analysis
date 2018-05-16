import language_tree
import langstrategy
import inspect
from routines import compute_cost_size_principle
import numpy as np

def aggregate_complexities():
	info = {}
	
	#assume naming convention is respected...	
	langlist = [i[0] for i in inspect.getmembers(langstrategy, inspect.isfunction) if len(i[0]) == 3] 
	
	for i in range(len(langlist)):
		complexity, num_type, ulim = language_tree.build_language(langlist[i])
		info[langlist[i]] = (complexity, num_type)

	return info

def aggregate_communicative_costs(need_probs, lang_info):
	"""lang_info should be a dict organized as {lang:(comp, num_type)}"""
	lang_by_category = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
	print(lang_info.items())
	for item in lang_info.items():
		lang_by_category[item[1][1]].append(item[0])	
	costs = {}

	#Restricted approximate systems
	for lang in lang_by_category[0]:
		#costs[lang] = compute_cost_approx()
		pass
	#Restricted exact systems
	for lang in lang_by_category[1]:
		ulim = [language_tree.build_language(lang)[2] for lang in lang_by_category[1]]
		costs[lang] = update_with_cost(len(lang_by_category[1]), lang_info[lang], ulim, need_probs)

	return costs


def update_with_cost(N, lang_info, upper_lim, nd):
	total_cost = 0
	for i in range(N):
		L_i = compute_cost_size_principle(upper_lim, nd)
		Cost_i = math.log(L_i, 2)
		Expected_i = nd[i] * Cost_i 
		total_cost += Expected_i
	return total_cost	
		
		


if __name__ == "__main__":

	c = aggregate_complexities()
	f = open("data/need_probs/need_probs.csv")
	need_probs = np.asarray([float(i) for i in f.read().split("\r\n")[:-1]])
	#print(need_probs)
	#print(c)
	print(aggregate_communicative_costs(need_probs, c))
	#print(aggregate_communicative_costs())

	
