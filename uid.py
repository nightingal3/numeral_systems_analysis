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


def calc_entropy_trajectory(df, need_prob, *opts):
	eng_dict = {"one": 1, "two": 2, "three": 3, "thir": 3, "four": 4, "five": 5, "fif": 5, "six": 6, "seven": 7, "eight": 8, "eigh": 8, "nine": 9, "teen": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "twenty": 20, "thirty": 30, "fourty": 40}	
	eng_dict = pd.Series(df.Number.values, index=df.Reading).to_dict()
	eng_dict.update({"twen": 2, "thir": 3, "fif": 5, "eigh": 8, "teen": 10, "eleven": 11, "twelve": 12})
	inv_eng_dict = {val: key for key, val in eng_dict.items()}
	entropies = [val * math.log(1/float(val), 2) for val in need_prob] 
	#base_H = sum(entropies)
	H_traj_dict = {}

	for opt in opts:
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
					print(curr)
					#print(selected_vals)
					
					#need_prob = [val for i, val in enumerate(need_prob) if i in selected_vals]
				
				else:
					curr = phrase[j]
					print(curr)
					selected_vals = [i for i in range(1, 101)]

				H, selected_vals = calc_conditional_probability(curr, curr_num, need_prob, eng_dict, inv_eng_dict, selected_vals)
				H_seq.append(H)

                        H_traj_dict[curr_num] = H_seq

        UID_dev = {}
        for traj in H_traj_dict:
                UID_dev[traj] = calc_UID_deviation(H_traj_dict[traj], len(inv_eng_dict[traj].split("-")))

	return H_traj_dict, UID_dev

def calc_conditional_probability(word, target, need_prob, num_dict, inv_num_dict, numberline):
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
	print(target)
	print(selected_vals)
	print(need_prob)
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
        print(selected_vals)
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
			I = H_traj[i] - H_traj[i + 1]
		print(I)
		total += abs(float(I)/float(H_traj[0]) - (1/float(phrase_len)))

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
	print("H_traj")
	H_trajs, UID_dev = calc_entropy_trajectory(df, need_probs, eng_words)
	print(H_trajs, UID_dev)
	lists = sorted(UID_dev.items())
	x, y = zip(*lists)
	#fifteen = H_trajs[25]
	#print(fifteen)
	plt.plot(x, y)
	plt.xlabel("Number")
	plt.ylabel("UID deviation score")
	plt.savefig("UID_dev.png")
	
