import numpy as np

def get_term_num_matrix(term, nnum, num_term_pt, end_category, numberline):
	nterm = len(term)
	
	#last term closes and is exact numeral
	if end_category == 1  and len(numberline) > len(num_term_pt):
		nterm += 1
		num_term_pt.append([nterm] * (numberline - nterm))
	#last term opens and is approximate
	elif end_category == 0 and len(numberline) > len(num_term_pt):
		num_term_pt.append([num_term_pt[-1]] * (numberline - nterm))
	elif end_category == 0 and len(num_term_pt) > len(numberline):
		num_term_pt = num_term_pt[:nnum]
	
	term_num_map = np.zeros(nterm, nnum)
	for i in range(nterm):
		indices = [x for (x, val) in enumerate(num_term_pt) if val == i]
		for x in indices:
			term_num_map[i, x] = 1
		#term_num_map[i, find(num_term_pt, lambda x: x == i)] = 1

	return term_num_map, nterm	


