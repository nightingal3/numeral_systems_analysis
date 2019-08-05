import math

def compute_cost_approx(term, numberline, num_term_pt, end_category, nd, mu_range=range(21), w=0.31):
	
	cc = 1 / (math.sqrt(2) * w)
	nnum = len(numberline)
	term_num_map, nterms = get_term_num_matrix(term,nnum,num_term_pt,end_category,numberline)
	#Find optimal mus
	a, mmap = max(term_num_map), np.indmax(term_num_map)
	
	#Compute communicative cost
	log_prob_L = math.log(log_prob_L, 2)
	c = sum(np.multiply(nd, np.multiply(log_prob_L, -1)))

	return c
