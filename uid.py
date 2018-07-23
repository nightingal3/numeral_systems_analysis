import matplotlib
matplotlib.use("Agg")
import pandas as pd
import math
import sys
from routines.find import *
from routines.my_enumerate import *
import matplotlib.pyplot as plt
import itertools
import pickle
import csv
import scipy.stats

def do_plot(**langs, opt="all"):
	"""Just call this function to plot things.
	opts: all (UID, RAG, mini UID/RAG plots, plots for groups of 10)
	uid: UID, mini plots
	rag: RAG, mini plots
	10s: plots for groups of 10"""
	number, lang_opts = read_file("atom_base.csv", 4)
	word_order_langs = {}
	for i, lang_name in new_enumerate(langs, 0, 2):
                title = lang_name + "_words"
                title_alt = lang_name + "_alt"
                word_order_langs[title] = lang_opts[i]
                word_order_lang[title_alt] = lang_opts[i + 1]


        #not done
        return
        



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
	curr_dict.update({"twen": 2, "thir": 3, "fif": 5, "eigh": 8, "teen": 10, "eleven": 11, "twelve": 12})
	inv_dict = {val: key for key, val in curr_dict.items()}
	alt_dict = {"-".join(key.split("-")[::-1]): val for key, val in curr_dict.items()}
	del alt_dict["teen-eigh"]
	alt_dict["teen-eight"] = 18
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
        #now called RAG (rapid information gain)
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
	i = 0
        colors = itertools.cycle(["green", "red", "b", "c", "m", "y", "k", "#e89600"])
        for name in area_dict:
                points_x = []
                points_y = []
                for num in area_dict[name]:
                        points_x.append(num)
                        points_y.append(area_dict[name][num])

                plt.bar(points_x, points_y, color=next(colors), label=name, alpha=0.5)

        plt.xlabel("Number")
        plt.xticks([i for i in range(10, 100, 10)])
        plt.ylabel("Surprisal (bits)")
        plt.legend()
        plt.savefig("Area.png")
        plt.gcf().clear()


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


def plot_avg_bars(dict1, dict2, lang):
	costs_1 = {}
	costs_2 = {}
	for i in range(10, 100, 10):
		costs_1[i] = []
		costs_2[i] = []

	for num in dict1:
		costs_1[(num / 10) * 10].append(dict1[num])
		costs_2[(num / 10) * 10].append(dict2[num])

	final_1 = []
	mse_1 = []
	final_2 = []
	mse_2 = []
	for num in sorted(costs_1):
		total = 0
		for cost in costs_1[num]:
			total += cost
		avg = float(total) / float(len(costs_1[num]))
		final_1.append(avg)
		mse_1.append(scipy.stats.sem(costs_1[num]))


		total = 0
		for cost in costs_2[num]:
			total += cost
		avg = float(total) / float(len(costs_2[num]))
		final_2.append(avg)
		mse_2.append(scipy.stats.sem(costs_2[num]))

	print(final_2)
	print(mse_2)
        plt.gcf().clear()
        plt.title("Cumulative surprisal (range of 10)", fontsize="x-large")
	plt.bar([num for num in sorted(costs_1.keys())], final_1, yerr=mse_1, width=3, color="red", alpha=0.75, label="Attested")
	plt.bar([num + 3 for num in sorted(costs_2.keys())], final_2, yerr=mse_2, width=3, color="green", alpha=0.75, label="Alternate")
	plt.legend(fontsize="x-large")
	plt.xlabel("Number", fontsize="x-large")
	plt.ylabel("Surprisal (bits)", fontsize="x-large")
	plt.savefig("test.png")
	
if __name__ == "__main__":
	number, lang_opts = read_file("atom_base.csv", 4)
	#print(lang_opts)

	eng_words, eng_mod, mand_words, mand_mod = lang_opts
	f_np = open("data/need_probs/need_probs.csv", "r")
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
	total = 0
	for i in range(len(need_probs_mnd_smooth)):
		total += need_probs_mnd_smooth[i]
	need_probs_mnd_smooth = [float(x)/float(total) for x in need_probs_mnd_smooth]
	H_trajs, UID_dev = calc_info_trajectory(df, need_probs, eng=eng_words, eng_alt=eng_mod)
        #plot_avg_bars(UID_dev["mand"], UID_dev["mand_alt"], "eng")
        
	area = calc_UTC(eng=H_trajs["eng"], mand_alt=H_trajs["eng_alt"])
	#plot_avg_bars(area["eng"], area["eng_alt"], "eng")
	#plot_area(area)
	
	
	mand_reg = UID_dev["eng"]
	mand_alt = UID_dev["eng_alt"]
        
	for num in H_trajs["eng"]:
                if num % 10 == 0:
                        continue
               	title = str(num) + " (English)"
                plt.title(title, fontsize="x-large")
                plt.plot([0, 1, 2], H_trajs["eng"][num], color="blue", label="fif-teen") #attested
                plt.plot([0, 1, 2], H_trajs["eng_alt"][num], color="orange", label="teen-fif") #alternate
		plt.plot([0, 1, 2], [H_trajs["eng"][num][0], H_trajs["eng"][num][0] / 2, 0], color="red", label="UID")
                name = "uid/" + str(num) + ".png"
                plt.xlabel("Number of words", fontsize="x-large")
                plt.xticks([0, 1, 2])
                plt.ylabel("Surprisal (bits)", fontsize="x-large")
                plt.legend(fontsize="x-large")
                plt.savefig(name)
                plt.gcf().clear()
	
	assert False
        
	lists = sorted(mand_reg.items())
	lists = [item for item in lists if item[0] % 10 != 0]
	lists1 = sorted(mand_alt.items())
	lists1 = [item for item in lists1 if item[0] % 10 != 0]
	
	x, y = zip(*lists)
	x1, y1 = zip(*lists1)
	#plt.plot(x, y, color="red", label="English attested")
        plt.bar(x1, y1, color="green", label="English alternate", alpha=0.5)
	plt.bar(x, y, color="red", label="English attested", alpha=0.5)
	#plt.plot(x1, y1, color="green", label="English alternate")
	
	plt.xlabel("Number")
	plt.ylabel("UID deviation score")
	plt.legend()
	plt.savefig("UID_dev.png")
	plt.gcf().clear()
