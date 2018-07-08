import matplotlib
matplotlib.use("Agg")
import pandas as pd
import math
import sys
from routines.find import *
import matplotlib.pyplot as plt


def read_file(filename):
	f = open(filename, "r");
	number = []
	eng_words = []
	eng_mod = []
	chn_words = []
	chn_mod = []

	for line in f.readlines():
		split_line = line.split(",")
		number.append(int(split_line[0]))
		eng_words.append(split_line[1].split("-"))
		eng_mod.append(split_line[2].split("-"))

	f.close()
	return number, eng_words, eng_mod


def calc_entropy_trajectory(df, need_prob, **opts):	
	eng_dict = pd.Series(df.Number.values, index=df.Reading).to_dict()
	eng_dict.update({"twen": 2, "thir": 3, "fif": 5, "eigh": 8, "teen": 10, "eleven": 11, "twelve": 12})
	inv_eng_dict = {val: key for key, val in eng_dict.items()}
	alt_eng_dict = {"-".join(key.split("-")[::-1]): val for key, val in eng_dict.items()}
	del alt_eng_dict["teen-eigh"]
	alt_eng_dict["teen-eight"] = 18
	inv_alt_eng_dict = {val: key for key, val in alt_eng_dict.items()}
	entropies = [val * math.log(1/float(val), 2) for val in need_prob] 
	H_traj_dict = {}

	for name, opt in opts.items():
		if name == "eng":
			curr_dict = eng_dict
			inv_dict = inv_eng_dict
		elif name == "eng_alt":
			curr_dict = alt_eng_dict
			inv_dict = inv_alt_eng_dict

		H_traj_dict[name] = {}

		for i in range(len(number)):
			curr_num = number[i]
			phrase = opt[i]
			selected_vals = []
			base_H = need_prob[curr_num]
			H_seq = [base_H]
			for j in range(len(phrase)):
				curr = ''
				if j > 0:
					if phrase[j] == "ty":
						curr = phrase[j - 1] + phrase[j]

					elif phrase[j - 1] == "ty":
                                                curr = phrase[j - 2] + phrase[j - 1] + "-" + phrase[j]
					else:
						curr = phrase[j - 1] + '-' + phrase[j]
				
				else:
					curr = phrase[j]
					selected_vals = [i for i in range(1, 101)]

				H, selected_vals = calc_conditional_probability_reconst_cost(curr, curr_num, need_prob, curr_dict, inv_dict, selected_vals)
				H_seq.append(H)

                        H_traj_dict[name][curr_num] = H_seq

        UID_dev = {}
	for name, opt in opts.items():
		UID_dev[name] = {}		
        for opt in H_traj_dict:
		for traj in H_traj_dict[opt]:
                	UID_dev[opt][traj] = calc_UID_deviation(H_traj_dict[opt][traj], len(inv_eng_dict[traj].split("-")))

	return H_traj_dict, UID_dev

def calc_conditional_probability_reconst_cost(word, target, need_prob, num_dict, inv_num_dict, numberline):
	word_val = num_dict[word]
	selected_vals = []
	irregulars = ["twen", "thir", "fif"]
	for num in numberline:
		if (word_val == num and word not in irregulars) or (len(str(num)) > 1 and word == inv_num_dict[num][:len(word)]):
			selected_vals.append(num)
	need_prob = [val for i, val in enumerate(need_prob) if i + 1 in selected_vals]
	if sum(need_prob) == 0:
		print("Error: word '%s' does not refer to any number. Ensure all input words are correct." % word)
		sys.exit(1);
	P_target = need_prob[find(selected_vals, target)[0]]
	P_all = sum(need_prob)

	return float(P_target) / float(P_all), selected_vals
	
def calc_conditional_entropy(word, need_prob, num_dict, inv_num_dict, numberline):
	"""Depreciated"""
	word_val = num_dict[word]
	selected_vals = []
	irregulars = ["twen", "thir", "fif", "eigh"]
	for num in numberline:
		if (word_val == num and word not in irregulars) or (len(str(num)) > 1 and word == inv_num_dict[num][:len(word)]):
			selected_vals.append(num)
        need_prob = [val for i, val in enumerate(need_prob) if i + 1 in selected_vals]
	
	if sum(need_prob) == 0:
		print("Error: word '%s' does not refer to any number. Ensure all input words are correct." % word)
		sys.exit(1);
	entropies = [(need_prob[i]/sum(need_prob)) * math.log(1/float(need_prob[i]/sum(need_prob)), 2) for i, val in enumerate(selected_vals)]

	return sum(entropies), selected_vals


def calc_UID_deviation(H_traj, phrase_len):
	total = 0
	if phrase_len == 1:
                return 0
        
	for i in range(phrase_len):
		if i == phrase_len - 1:
			I = H_traj[-2]
		else:
			I = H_traj[i + 1] - H_traj[i]
		
		total += abs(float(I) - (1/float(phrase_len)))
	return (float(phrase_len)/float(phrase_len + 1)) * total


def calc_UTC(*H_traj):
	#UTC stands for Uncertainty over Time Cost
	raise NotImplementedError


def plot_UID_vs_UTC(*H_traj):
        raise NotImplementedError

if __name__ == "__main__":
	number, eng_words, eng_mod = read_file("atom_base.csv")
	f_np = open("data/need_probs/need_probs.csv", "r")
	f_num = pd.read_csv("data/terms_1_to_100/english.csv")
	number_words = f_num["Reading"].values.tolist()
	df = pd.read_csv("data/terms_1_to_100/english.csv")
	need_probs = [float(i) for i in f_np.read().split("\r\n")[:-1]]
	H_trajs, UID_dev = calc_entropy_trajectory(df, need_probs, eng=eng_words, eng_alt=eng_mod)
	eng_reg = UID_dev["eng"]
	eng_alt = UID_dev["eng_alt"]
	lists = sorted(eng_reg.items())
	lists = [item for item in lists if item[0] % 10 != 0]
	lists1 = sorted(eng_alt.items())
	lists1 = [item for item in lists1 if item[0] % 10 != 0]
	x, y = zip(*lists)
	x1, y1 = zip(*lists1)
	plt.plot(x, y, color="blue", label="English attested")
	plt.plot(x1, y1, color="orange", label="English alternate")
	plt.xlabel("Number")
	plt.ylabel("UID deviation score")
	plt.legend()
	plt.savefig("UID_dev.png")
	plt.gcf().clear()
