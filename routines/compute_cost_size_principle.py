import numpy as np
import math

def compute_cost_size_principle(upper_lim, need_prob):
	length = len(need_prob)
	unit_cost = [0] * length
	denom = float(length - (upper_lim + 1) + 1)
	for i in range(upper_lim, length):
		unit_cost[i] = math.log(1/denom, 2) * -1
	
	c = sum(np.multiply(need_prob, unit_cost))
	return c


if __name__ == "__main__":
	need_prob_f = open("../data/need_probs/needprobs_eng_fit.csv", "r")
	need_prob = need_prob_f.read().split('\r\n')[:-1]
	need_prob = [float(i) for i in need_prob]
	need_prob_f.close()
	print(compute_cost_size_principle(3, need_prob))
