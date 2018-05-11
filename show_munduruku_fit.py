import matplotlib
matplotlib.use("Agg")
import sys
sys.path.insert(0, "routines")
import numpy as np
import matplotlib.pyplot as plt
import itertools
import math
#from routines import compute_P_w_i_correct_subitized
from routines import compute_P_w_i_bias_correct_subitized

def show_munduruku_fit(percent_file, terms_file, term_interp_file):
	#Data is from Pica(2004)
	subrange = [1, 2, 3]
	mu_range =  []
	mu_range.extend(range(1, 16))
	w = 0.31	
	c = 1 / (math.sqrt(2)*w)
	
	numberline = mu_range
	percent = np.loadtxt(open(percent_file, "rb"), delimiter=",").astype("float")
	terms = np.loadtxt(open(terms_file, "rb"), delimiter=",", dtype="string")
	term_interp = np.loadtxt(open(term_interp_file, "rb"), delimiter=",", dtype="string")
	nnum, ncat = 15, terms.shape[0]
	
	bias = 55 * percent
	bias = np.sum(bias, axis=1)
	bias = bias / np.sum(bias)
		
	total_mass = np.sum(percent, axis=0)
	total_mass[1:4] = 1
	
	mu_placements = np.array(list((itertools.combinations(mu_range, ncat))))
	n_placements = mu_placements.shape[0]
	
	#Plot Munduruku data
	colors = itertools.cycle(["r", "g", "b", "c", "m", "y", "k", "#e89600"])
	title0 = itertools.cycle(terms)
	title1 = itertools.cycle(term_interp)

	fig, (ax_data, ax_model) = plt.subplots(1, 2, sharey=True)
	for row in percent:
		ax_data.plot(numberline, row, next(colors), label=next(title0) + "=" + next(title1))
	
	#Plot model data
	P_w_i_opt = None
	min_mse = float("inf")
	mu_opt = None
       	print(n_placements) 
	for i in range(n_placements):
		mus = mu_placements[i, :]
		#print(mu_placements.shape)	
		#print(mus.shape)
		#print(total_mass)
		#print(total_mass.shape)
		#print(nnum, ncat, mus, c, w, total_mass, subrange, bias)
		P_w_i = compute_P_w_i_bias_correct_subitized(nnum, ncat, mus, c, w, total_mass, subrange, bias)
		#print(nnum, ncat, mus, c, w, total_mas, subrange, bias)
		mse_curr = np.mean(np.mean((P_w_i[:, :percent.shape[1]] - percent) ** 2, axis=1))
		#print(mse_curr)
		if mse_curr < min_mse:
			min_mse = mse_curr
			P_w_i_opt = P_w_i
			mu_opt = mus

	#print(P_w_i_opt)
	print(min_mse)
	for row in P_w_i_opt:
		ax_model.plot(numberline, row, next(colors)) 

	handles, labels = ax_data.get_legend_handles_labels()
	fig.legend(handles, labels, loc="upper right", prop={"size":5})
	ax_data.set_xlabel("Number line")
	ax_model.set_xlabel("Number line")
	ax_data.set_ylabel("Response frequency")
	ax_model.set_ylabel("P(w|i)")			
	plt.savefig("mund_comp.png", dpi=1000)
	return

if __name__ == "__main__":
	show_munduruku_fit("data/munduruku_pica2004/percent.csv", "data/munduruku_pica2004/terms.csv", "data/munduruku_pica2004/term_interp.csv")
