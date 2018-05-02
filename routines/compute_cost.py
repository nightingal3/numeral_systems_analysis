import numpy

def compute_approx_cost(nargin, term, numberline, num_term_pt, end_category, nd, mu_range, w):
	if nargin < 7:
		mu_range = range(1:21)
		w = 0.31
	else if nargin < 8:
		w = 0.31
	cc = 1 / (sqrt(2) * w)
	nnum = len(numberline)

	(term_num_map, nterm) = get_term_num_matrix(term, nnum, num_term_pt, end_category, numberline)
	a = max(term_num_map)
	mmap = term_num_map.index(a)
	(mus, P_w_i_vec) = compute_P_w_i_match_modemap1(mmap, numberline, nterm, term_num_map, mu_range, c, w, nd)
	
	F_i_w_numerator = compute_f_i_w_numerator(nnum, nterm, numberline, mus, cc, w)
	
	log_prob_L = zeros(1, nnum)
	
	for j in range(1, nterm):
		cat_inds = [i for i in mmap if i == j]
		f = F_i_w_numerator(j, cat_inds)
		log_prob_L(cat_inds) = f / sum(f)
	
	log_prob_L = math.log(log_prob_L, 2)
	c = numpy.multiply(nd, -log_prob_L)

	return c

