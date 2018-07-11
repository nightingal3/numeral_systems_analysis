import matplotlib
matplotlib.use("Agg")
import pandas as pd
import math
import sys
from routines.find import *
import matplotlib.pyplot as plt
import itertools
import pickle
import csv

def read_file(filename, num_opts):
	f = open(filename, "r");
	number = []
	langs = []
	for i in range(num_opts):
                langs.append([])

	for line in f.readlines():
		split_line = line.split(",")
		number.append(int(split_line[0]))
		
                for j in range(len(langs)):
                        if j == len(langs) - 1:
                                langs[j].append(split_line[j + 1][:-2].split("-")) #for some reason lines end with \r\n
                        else:
                                langs[j].append(split_line[j + 1].split("-"))
                                

	f.close()
	return number, langs


def calc_info_trajectory(df, need_prob, **opts):	
	curr_dict = pd.Series(df.Number.values, index=df.Reading).to_dict()
	#curr_dict.update({"twen": 2, "thir": 3, "fif": 5, "eigh": 8, "teen": 10, "eleven": 11, "twelve": 12})
	inv_dict = {val: key for key, val in curr_dict.items()}
	alt_dict = {"-".join(key.split("-")[::-1]): val for key, val in curr_dict.items()}
	#del alt_eng_dict["teen-eigh"]
	#alt_eng_dict["teen-eight"] = 18
	inv_alt_dict = {val: key for key, val in alt_dict.items()}
	entropies = [val * math.log(1/float(val), 2) for val in need_prob] 
	H_traj_dict = {}

	for name, opt in opts.items():
                if name[-3:] == "alt":
                        curr_tmp = curr_dict
			curr_dict = alt_dict
			inv_tmp = inv_dict
			inv_dict = inv_alt_dict

		else:
                        curr_dict = curr_tmp
                        inv_dict = inv_tmp
			
		"""if name == "eng":
			curr_dict = eng_dict
			inv_dict = inv_eng_dict
		elif name == "eng_alt":
			curr_dict = alt_eng_dict
			inv_dict = inv_alt_eng_dict

		elif name == "mand":
                        pass

                elif name == "mand_alt":
                        pass"""

		H_traj_dict[name] = {}

		for i in range(len(number)):
			curr_num = number[i]
			phrase = opt[i]
			selected_vals = []
			base_H = math.log(1/need_prob[curr_num], 2)
			H_seq = [base_H]
			if len(phrase) == 1:
                                continue
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
                	UID_dev[opt][traj] = calc_UID_deviation(H_traj_dict[opt][traj], len(inv_dict[traj].split("-")))

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

	print(word)
	print(selected_vals)
        print(need_prob)
	print("target:" + str(target))
	P_target = need_prob[find(selected_vals, target)[0]]
	P_all = sum(need_prob)
        
        print(math.log(float(P_all) / float(P_target), 2))
        return math.log(float(P_all) / float(P_target), 2), selected_vals
        #return float(P_target) / float(P_all), selected_vals
	
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
        
	for i in range(1, phrase_len):
		total += abs(H_traj[i]/H_traj[0] - (1/float(phrase_len)))
		
	return total


def calc_UTC(**H_traj):
	#UTC stands for Uncertainty over Time Cost
	area = {}
	for name, opt in H_traj.items():
		area[name] = {}
		for traj in H_traj[name]:
                        area[name][traj] = 0
                        for i in range(len(H_traj[name][traj])):
                                area[name][traj] += H_traj[name][traj][i]
		
	return area			



def plot_area(area_dict):
	print(area_dict)
        colors = itertools.cycle(["m", "#1b5f7c", "b", "c", "m", "y", "k", "#e89600"])
        for name in area_dict:
                points_x = []
                points_y = []
                for num in area_dict[name]:
                        points_x.append(num)
                        points_y.append(area_dict[name][num])

                plt.plot(points_x, points_y, color=next(colors), label=name)

        plt.xlabel("Number")
        plt.xticks([i for i in range(10, 100, 10)])
        plt.ylabel("Surprisal (bits)")
        plt.legend()
        plt.savefig("Area.png")
        plt.gcf().clear()

        
def plot_UID_vs_UTC(*H_traj):
        raise NotImplementedError


def normalize_freq(freqs, upper_lim):
	total = 0
	new = {}
	for num in freqs:
		if int(num) in range(1, upper_lim + 1):
			total += freqs[num]
			new[int(num)] = freqs[num]

	for num in new:
		new[num] /= float(total)

	return new

if __name__ == "__main__":
	number, lang_opts = read_file("atom_base.csv", 4)
	#print(lang_opts)

	eng_words, eng_mod, mand_words, mand_mod = lang_opts
	f_np = open("data/need_probs/needprobs_eng_fit.csv", "r")
	f_np_all = open("total_word_freq.p", "rb")
	"""digit_freq_all = pickle.load(f_np_all)
	digit_freq_mand = digit_freq_all["chinese"]
	digit_freq_mand = normalize_freq(digit_freq_mand, 100)
	mand_need_prob = []
	print(sorted(digit_freq_mand.iterkeys()))
	for key in sorted(digit_freq_mand.iterkeys()):
		mand_need_prob.append(digit_freq_mand[key])

	with open('data/need_probs/needprobs_mand.csv', 'wb') as myfile:
    		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    		wr.writerow(mand_need_prob)
	"""
	f_np_mnd = open("data/need_probs/needprobs_mand.csv", "r")
	f_num = pd.read_csv("data/terms_1_to_100/english.csv")
	f_num_mand = pd.read_csv("data/terms_1_to_100/chinese_romanized.csv")
	number_words = f_num["Reading"].values.tolist()
	number_words_mand = f_num["Reading"].values.tolist()
	df_m = pd.read_csv("data/terms_1_to_100/chinese_romanized.csv")
	df = pd.read_csv("data/terms_1_to_100/english.csv")
	need_probs = [float(i) for i in f_np.read().split("\r\n")[:-1]]
	need_probs_mnd = [float(i) for i in f_np_mnd.read().split("\r\n")[:-1]]
	need_probs_mnd_smooth = [-0.018 * math.log(i) + 0.0738 for i in need_probs_mnd]
	H_trajs, UID_dev = calc_info_trajectory(df_m, need_probs_mnd_smooth, mand=mand_words, mand_alt=mand_mod)
        print(H_trajs)
        
	area = calc_UTC(mand=H_trajs["mand"], mand_alt=H_trajs["mand_alt"])
	plot_area(area)
	
	
	mand_reg = UID_dev["mand"]
	mand_alt = UID_dev["mand_alt"]
        
	for num in H_trajs["mand"]:
                if num % 10 == 0:
                        continue
                title = str(num) + " (Mandarin)"
                plt.title(title)
                plt.plot([0, 1, 2], H_trajs["mand"][num], color="blue", label="Attested")
                plt.plot([0, 1, 2], H_trajs["mand_alt"][num], color="orange", label="Alternate")
                name = "uid/mand" + str(num) + ".png"
                plt.xlabel("Number of words")
                plt.xticks([0, 1, 2])
                plt.ylabel("Surprisal (bits)")
                plt.legend()
                plt.savefig(name)
                plt.gcf().clear()

        
	lists = sorted(mand_reg.items())
	lists = [item for item in lists if item[0] % 10 != 0]
	lists1 = sorted(mand_alt.items())
	lists1 = [item for item in lists1 if item[0] % 10 != 0]
	
	x, y = zip(*lists)
	x1, y1 = zip(*lists1)
	plt.plot(x, y, color="cyan", label="Mandarin attested")
	plt.plot(x1, y1, color="purple", label="Mandarin alternate")
	plt.xlabel("Number")
	plt.ylabel("UID deviation score")
	plt.legend()
	plt.savefig("UID_dev.png")
	plt.gcf().clear()
