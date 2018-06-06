import numpy as np
import math
from random import randint
from compute_cost import compute_f_i_w_numerator
from find import *

def test_gauss_blob_place_mu_greedy(nnum, nterm, numberline, mu_range, c, w, need_probs, nsamp, optdir, subrange=[i for i in range(3)]):
	comp_perm = []
	ccost_perm = []
	comp_perm_ns = []
	ccost_perm_ns = []
	f = float("inf")
	
	mus_init = [i for i in range(1, max(mu_range), max(mu_range)/(nterm+2))][1:-1]
	
	for ii in range(20):
		mus = np.asarray(np.random.permutation(max(mus_init))[:nterm]).transpose()
		cost_prev = compute_cost_comp(nnum, nterm, numberline, mus, c, w, need_probs, subrange)	
		for jj in range(nsamp):
			seq = np.random.permutation(nterm)
			flag = 1
			for i in range(nsamp):
				coin = randint(0, 1)
				mus_propose = propose_mus(mus, max(mu_range), seq[i], coin)
				ccost_perm_t, ccost_perm_ns_t, comp_perm_t, comp_perm_ns_t = compute_cost_comp(nnum, nterm, numberline, mus, c, w, need_probs, subrange)
				if optdir < 0:
					flag = ccost_perm_t < costprev
				else:
					flag = ccost_perm_t > costprev
	
				if flag:
					comp_perm = [comp_perm, comp_perm_t, comp_perm_ns_t]
					ccost_perm = [ccost_perm, ccost_perm_t, ccost_perm_ns_t]
					currdiff = abs(costprev - ccost_perm_t)
					cost_prev = ccost_perm_t
					mus = mus_propose
						
					 
	
	return comp_perm, ccost_perm


def compute_cost_comp(nnum, nterm, numberline, mus, c, w, need_probs, subrange):
	F_i_w_numerator = compute_f_i_w_numerator(nnum, nterm, numberline, mus, c, w)
	term_num_map = np.zeros((nterm, nnum))
	print(np.max(F_i_w_numerator, 0))
	print(find(F_i_w_numerator, np.max(F_i_w_numerator, 0)))
	#maxind = find(F_i_w_numerator, max(F_i_w_numerator))[0]
	maxmaxind = find(maxind, max(maxind))
	maxind[maxmaxind[-1] + 1:] = max(maxind)

	for i in range(1, nterm):
		inds = find(maxind, i)
		for ind in inds:
			term_num_map[i, ind] = 1

	for diff_ind in find_diff(numberline, find(sum(term_num_map), 1)):
		term_num_map[nterm, diff_ind] = 1
	
	mmap = max(term_num_map)
	log_prob_L = np.zeros((1, nnum))
	
	for j in range(1, nterm): 
		cat_inds = find(mmap, j)
		f = F_i_w_numerator[j, cat_inds]
		log_prob_L[cat_inds] = f / sum(f)

	log_prob_L = math.log(log_prob_L, 2)

	ccost_perm = np.sum(needprobs * -log_prob_L)
	comp_perm_ns = 3 * length(find_unique(mmap))

	return ccost_perm, ccost_perm_ns, comp_perm, com_perm_ns



def propose_mus(mus, maxval, i, optdir):
	mus_new = mus
	end_sig = 0
	if optdir <= 0: #minimizing dir (go left)
		if i == 0:
			if mus[0] > 1: 
				mus_new[i] = mus[i] - 1 
			else:
				end_sig = 1
		else:
			if mus[i] > mus[i - 1]: 
				mus_new[i] = mus[i] - 1
			else: 
				end_sig = 1
	else: #maximizing dir (go right)
		if i == length(mus):
			if mus[-1] < maxval: 
				mus_new[i] = mus[i] + 1
			else: 
				end_sig = 1
		else:
			if mux[i] < mus[i+1]:
				 mus_new[i] = mus[i] + 1 
			else:
				 end_sig = 1

	return mus_new, end_sig			

if __name__ == "__main__":
	need_probs = open("../data/need_probs/needprobs_eng_fit.csv", "r").read().split("\r\n")
	#print(test_gauss_blob_place_mu_greedy(100, 2, [i for i in range(1, 101)], [i for i in range(1, 101)], 2.2810, 0.31, need_probs, 100, -1, [1, 2, 3]))
 	print(compute_cost_comp(100, 2, [ i for i in range(1, 101)], [8, 90], 2.2810, 0.31, need_probs, [1, 2, 3]))
	#print(find([1, 2, 3], 3))
