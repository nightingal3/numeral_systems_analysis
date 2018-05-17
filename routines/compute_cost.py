import numpy as np
from get_term_num_matrix import get_term_num_matrix
import math

def compute_approx_cost(term, numberline, num_term_pt, end_category, nd, mu_range, w):
	if len(locals()) < 7:
		mu_range = range(1, 21)
		w = 0.31
	elif len(locals()) < 8:
		w = 0.31
	cc = 1 / (math.sqrt(2) * w)
	nnum = len(numberline)

	term_num_map, nterm = get_term_num_matrix(term, nnum, num_term_pt, end_category, numberline)
	print(term_num_map)
	assert False
	a = max(term_num_map)
	mmap = term_num_map.index(a)
	(mus, P_w_i_vec) = compute_P_w_i_match_modemap1(mmap, numberline, nterm, term_num_map, mu_range, c, w, nd)
	
	F_i_w_numerator = compute_f_i_w_numerator(nnum, nterm, numberline, mus, cc, w)
	
	log_prob_L = zeros(1, nnum)
	"""
	for j in range(1, nterm):
		cat_inds = [i for i in mmap if i == j]
		f = F_i_w_numerator(j, cat_inds)
		log_prob_L(cat_inds) = f / sum(f)
	"""
	log_prob_L = math.log(log_prob_L, 2)
	c = np.multiply(nd, -log_prob_L)

	return c


def compute_cost_size_principle(upper_lim, need_prob):
	length = len(need_prob)
	unit_cost = [0] * length	
	denom = length - (upper_lim + 1) + 1
	for i in range(upper_lim, length):
		unit_cost[i] = -math.log(float(1)/float(length - (upper_lim + 1) + 1), 2)
	c0 = np.asarray(need_prob) * np.asarray(unit_cost) 

        return c0.sum()


def compute_cost_size_principle_arb(modemap, need_prob):
	l = len(nd)
	unit_cost = [0] * 1
	modemap_set = set(modemap)
	unique_cat = modemap_set
	
	for i in range(len(unique_cat)):
		inds = [j for (j, val) in enumerate(modemap) if modemap[j] == unique_cat[i]] 
		for ind in inds:
			unit_cost[ind] = -math.log(1/len(inds))

	return sum(np.multiply(need_prob, unit_cost))
			

if __name__ == "__main__":
	f = open("data/need_probs/needprobs_eng_fit.csv")
	nd = [float(i) for i in f.read().split("\r\n")[:-1]]
	compute_approx_cost(["hoi1", "hoi2", "aibaagi"], [i for i in range(101)], [1, 2, 2, 2, 3, 3, 3, 3, 3, 3], 0, nd, [i for i in range(20)], 0.31)
