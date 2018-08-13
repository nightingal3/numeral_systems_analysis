#-*- coding: utf-8 -*-
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
import scipy.stats

def generate_attested_and_alternate(filename):
	#given a file containing terms in a range, generate the attested and reverse and return in same format as read_file
	#here because of the implementation I chose which doesn't entirely make sense now...oh well
	f = open(filename, "r")
	number = []
        attested_opt = []
	alternate_opt =  []

	for line in f.readlines()[1:]:
		split_line = line.split(",")
		number.append(int(split_line[0]))
		attested = split_line[1].strip("\r\n").split("-")
		reverse = split_line[1].strip("\r\n").split("-")[::-1]
		attested_opt.append(attested)
		alternate_opt.append(reverse)

	return number, attested_opt, alternate_opt

	
def read_file(filename, num_opts):
	f = open(filename, "r")
	number = []
	langs = []
	for i in range(num_opts):
                langs.append([])

	for line in f.readlines():
		split_line = line.split("\t")
		number.append(int(split_line[0]))
		
                for j in range(len(langs)):
                        if j == len(langs) - 1:
                                langs[j].append(split_line[j + 1][:-2].split("-")) #for some reason lines end with \r\n
                        else:
                                langs[j].append(split_line[j + 1].split("-"))
                                

	f.close()
	return number, langs


def calc_info_trajectory(df, need_prob, langname, maxval, **opts):	
	curr_dict = pd.Series(df.Number.values, index=df.Reading).to_dict()
        irregulars = {}	
        #~~~~Special language spelling handling~~~~
	if langname[:3] == "eng":
                curr_dict.update({"twen": 2, "thir": 3, "fif": 5, "eigh": 8, "teen": 10, "eleven": 11, "twelve": 12})
                separator = None
                if langname == "eng_1000":
                        irregulars = {"onehundred-and": 100, "twohundred-and": 200, "threehundred-and": 300, "fourhundred-and": 400, "fivehundred-and": 500, "sixhundred-and": 600, "sevenhundred-and": 700, "eighthundred-and": 800, "ninehundred-and": 900}
                        curr_dict.update(irregulars)
        elif langname == "ger":
                curr_dict.update({"sech": 6, "sieb": 7, "einund": 1, "zweiund": 2, "dreiund": 3, "vierund": 4, "funfund": 5, "sechsund": 6, "siebenund": 7, "achtund": 8, "neunund": 9})
                separator = None
        elif langname == "spa":
                curr_dict.update({"dieci": 10, "treinta-y": 30, "cuarenta-y": 40, "cincuenta-y": 50, "sesenta-y": 60, "setenta-y": 70, "ochenta-y": 80, "noventa-y": 90})
                separator = "y"
        elif langname == "ita":
                curr_dict.update({"un": 1, "do": 2, "quattor": 4, "quin": 5, "se": 6, "dicia": 10,  "dici": 10, "vent": 20, "trent": 30, "quarant": 40, "cinquant": 50, "sessant": 60, "settant": 70, "ottant": 80, "novant": 90})
        elif langname == "fre":
                curr_dict.update({"vingt-et": 20, "trente-et": 30, "quarante-et": 40, "cinquante-et": 50, "soixante-et": 60})
        
	inv_dict = {val: key for key, val in curr_dict.items() if key not in irregulars}
	alt_dict = {"-".join(key.split("-")[::-1]): val for key, val in curr_dict.items()}

	if langname[:3] == "eng":
                #del alt_dict["teen-eigh"]
                alt_dict["teen-eight"] = 18
                teen_endings = ["-thir", "-fif", "-eigh"]
                for key in irregulars:
                        for teen in teen_endings:
                                hund_teen = key + teen
                                curr_dict[hund_teen] = curr_dict[key + teen + "-teen"]
                        

        if langname == "spa":
                alt_dict["uno-y"] = 1
                alt_dict["dos-y"] = 2
                alt_dict["tres-y"] = 3
                alt_dict["cuatro-y"] = 4
                alt_dict["cinco-y"] = 5
                alt_dict["seis-y"] = 6
                alt_dict["siete-y"] = 7
                alt_dict["ocho-y"] = 8
                alt_dict["nueve-y"] = 9
        if langname == "fre":
                alt_dict["un-et"] = 1
                alt_dict["onze-et"] = 11
                alt_dict["vingts"] = 20
                
       
	inv_alt_dict = {val: key for key, val in alt_dict.items()}
	entropies = [val * math.log(1/float(val), 2) for val in need_prob] 
	H_traj_dict = {}
	alt_first = False

	

	for name, opt in opts.items():
                if name[-3:] == "alt":
                        curr_tmp = curr_dict
			curr_dict = alt_dict
			inv_tmp = inv_dict
			inv_dict = inv_alt_dict
			alt_first = True

		elif alt_first:
                        curr_dict = curr_tmp
                        inv_dict = inv_tmp
			
	
		H_traj_dict[name] = {}

		for i in range(len(number)):
			curr_num = number[i]
			phrase = opt[i]
			print(phrase)
			selected_vals = []
			base_H = math.log(1/need_prob[curr_num - 1], 2)
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
                                                curr = phrase[0]
                                                for i in range(1, j + 1):
                                                        curr += "-" + phrase[i] 
						#curr = phrase[j - 1] + '-' + phrase[j]
				
				else:
					curr = phrase[0]
					selected_vals = [i for i in range(1, maxval)]


				H, selected_vals = calc_conditional_probability_reconst_cost(curr, curr_num, len(phrase), need_prob, curr_dict, inv_dict, langname, selected_vals)
				H_seq.append(H)
                                

                        H_traj_dict[name][curr_num] = H_seq

        UID_dev = {}
	for name, opt in opts.items():
		UID_dev[name] = {}		
        for opt in H_traj_dict:
		for traj in H_traj_dict[opt]:
                	UID_dev[opt][traj] = calc_UID_deviation(H_traj_dict[opt][traj], len(inv_dict[traj].split("-")))

	return H_traj_dict, UID_dev

def calc_conditional_probability_reconst_cost(word, target, target_len, need_prob, num_dict, inv_num_dict, langname, numberline):
        if word == "onehundred-and-thir":
                print("Yo")
        if word[-4:] == "-and":
                raw_word = word[:-4]
                word_val = num_dict[raw_word]

        elif (len(word.split('-')) > 1 and word.split('-')[1] == "vingts") and inv_num_dict[18].split("-")[0] == "huit": #un-vingts, deux-vingts are technically meaningless (formatting issue)
                word_val = None
        else:
                word_val = num_dict[word]
                
	selected_vals = []
	irregulars = []
	if langname[:3] == "eng":
                irregulars = ["twen", "thir", "fif"]
        elif langname == "ger":
                irregulars = ["zehn", "zwanzig", "dreisig", "vierzig", "funfzig", "sechzig", "siebzig", "achtzig", "neunzig"] #not technically irregular, only needed because I treated something like "einund" as one unit
        elif langname == "spa":
                irregulars = ["uno-y", "dos-y", "treinta-y", "cuatro-y", "cuarenta-y", "cinco-y", "cincuenta-y", "seis-y", "sesenta-y", "siete-y", "setenta-y", "ocho-y", "ochenta-y", "nueve-y", "noventa-y"]
        elif langname == "ita":
                irregulars = ["do", "quattor", "quin", "dici", "dicia"]
        elif langname == "fre":
                irregulars = ["vingt-et", "trente-et", "quarante-et", "cinquante-et", "soixante-et", "onze-et"]
                
	for num in numberline:
                minlen = min(len(word), len(inv_num_dict[num]))
                minmatch = word[:minlen] == inv_num_dict[num][:minlen]
                if len(word.split('-')) == target_len:
                        if word_val == num:
                                selected_vals.append(num)

                else:
                        if (word_val == num and word not in irregulars) or (len(str(num)) > 1 and minmatch):
                                if word == "teen" and num == 10:
                                        continue
                                if word[-4:] == "-and" and inv_num_dict[num] == raw_word:
                                        continue
                                elif (inv_num_dict[num] in irregulars and len(word.split('-')) > 1) and langname == "ger":
                                        continue
                                elif (num % 10 == 0 and word in irregulars) and langname == "spa":
                                        continue
                                elif (num == 10 and word == "dicia") and langname == "ita":
                                        continue
                                elif (num == 60 and len(word.split("-")) > 1) and langname == "fre":
                                        continue
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


def calc_UID_deviation(H_traj, phrase_len): #what is the coefficient in general?
	total = 0
	if phrase_len == 1:
                return 0
        
	for i in range(1, phrase_len + 1):
                        total += abs(float(H_traj[i - 1] - H_traj[i])/H_traj[0] - (1/float(phrase_len)))
                        #total += abs(float(H_traj[i]/H_traj[0]) - (1/float(phrase_len)))
                        
	if phrase_len > 2:
                total *= float(phrase_len)/(2 * (phrase_len - 1))
		
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



def plot_area(area_dict, langname, maxval):
	for key in area_dict:
                if key[-4:] == "_alt":
                        first = key
                else:
                        second = key

        points_alt_x = []
        points_alt_y = []
	for num in area_dict[first]:
                if num > maxval:
                        break
                points_alt_x.append(num)
                points_alt_y.append(area_dict[first][num])
        if langname == "Universal":
                plt.bar(points_alt_x, points_alt_y, color="green", label="base-atom", alpha=0.5)
        else:
                plt.bar(points_alt_x, points_alt_y, color="green", label=first, alpha=0.5)

        
        points_x = []
        points_y = []
	for num in area_dict[second]:
                if num > maxval:
                        break
                points_x.append(num)
                points_y.append(area_dict[second][num])
        if langname == "Universal":
                plt.bar(points_x, points_y, color="red", label="atom-base", alpha=0.5)
        else:
                plt.bar(points_x, points_y, color="red", label=second, alpha=0.5)

        plt.xlabel("Number")
        plt.xticks([i for i in range(10, maxval, maxval / 10)])
        plt.ylabel("Surprisal (bits)")
        plt.legend()
        plt.title("Rapid Information Gain (" + langname + ")")
        plt.savefig("Area_" + langname + ".png")
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


def plot_mini(H_trajs, langname, color1="blue", color2="orange"):
        alt = langname + "_alt"
        langname_proper = {"mand": "Mandarin","eng_1000": "English", "eng": "English", "fre": "French", "ger": "German", "ita": "Italian", "spa": "Spanish", "uni": "Universal"}
        for num in H_trajs[langname]:
                if num % 10 == 0:
                        continue
               	title = str(num) + " (" + langname_proper[langname] + ")"
                plt.title(title, fontsize="x-large")
                length = len(H_trajs[langname][num])
                numberline = [i for i in range(length)]
                print(H_trajs[langname][num])
                plt.plot(numberline, H_trajs[langname][num], color=color1, label="Attested") #attested
                plt.plot(numberline, H_trajs[alt][num], color=color2, label="Alternate") #alternate
                uid_traj = [H_trajs[langname][num][0]]

                frac = H_trajs[langname][num][0] / (length - 1)
                for i in range(1, length - 1):
                    uid_traj.append(H_trajs[langname][num][0] - i * frac)
                uid_traj.append(0)
                print("UID:")
                print(uid_traj)
		plt.plot(numberline, uid_traj, color="red", label="UID")
                name = "uid/" + langname + "/" + str(num) + ".png"
                plt.xlabel("Number of words", fontsize="x-large")
                plt.xticks(numberline)
                plt.ylabel("Surprisal (bits)", fontsize="x-large")
                plt.legend(fontsize="x-large")
                plt.savefig(name)
                plt.gcf().clear()

                
	
if __name__ == "__main__":
	number, eng_words_1000, eng_mod_1000 = generate_attested_and_alternate("data/terms_1_to_100/english_1000.csv")		
	#number, lang_opts = read_file("atom_base.csv", 12)
	#eng_words, eng_mod, mand_words, mand_mod, ger_words, ger_mod, spanish_words, spanish_mod, french_words, french_mod, italian_words, italian_mod = lang_opts
	
	f_np = open("data/need_probs/eng_num_pos.csv", "r")
	f_np_1000 = open("data/need_probs/eng_1_to_1000.csv", "r")
	f_np_all = open("data/need_probs/total_need_prob_num.csv", "rb")
	f_np_mnd = open("data/need_probs/chinese_need_prob.csv", "r")
	f_np_ger = open("data/need_probs/german_need_prob.csv", "r")
	f_np_spa = open("data/need_probs/spanish_need_prob.csv", "r")
	f_np_ita = open("data/need_probs/italian_num_pos.csv", "r")
	f_np_fre = open("data/need_probs/french_need_prob.csv", "r")


	f_num = pd.read_csv("data/terms_1_to_100/english.csv")
	f_num_mand = pd.read_csv("data/terms_1_to_100/chinese_romanized.csv")
	number_words = f_num["Reading"].values.tolist()
	number_words_mand = f_num["Reading"].values.tolist()
	
	df_m = pd.read_csv("data/terms_1_to_100/chinese_romanized.csv")
	df = pd.read_csv("data/terms_1_to_100/english.csv")
	df_g = pd.read_csv("data/terms_1_to_100/german_segmented.csv")
	df_s = pd.read_csv("data/terms_1_to_100/spanish_romanized.csv")
	df_i = pd.read_csv("data/terms_1_to_100/italian_romanized.csv")
	df_f = pd.read_csv("data/terms_1_to_100/french.csv")
	df_1000 = pd.read_csv("data/terms_1_to_100/english_1000.csv")

 	need_probs = [float(i) for i in f_np.read().split("\r\n")[:-1]]
	need_probs_1000 = [float(i) for i in f_np_1000.read().split("\r\n")[:-1]]
	need_probs_mnd = [float(i) for i in f_np_mnd.read().split("\r\n")[:-1]]
	need_probs_ger = [float(i) for i in f_np_ger.read().split("\r\n")[:-1]]
	need_probs_spa = [float(i) for i in f_np_spa.read().split("\r\n")[:-1]]
	need_probs_ita = [float(i) for i in f_np_ita.read().split("\r\n")[:-1]]
	need_probs_fre = [float(i) for i in f_np_fre.read().split("\r\n")[:-1]]
	need_probs_all = [float(i) for i in f_np_all.read().split("\r\n")[:-1]]
	
	H_trajs, UID_dev = calc_info_trajectory(df_1000, need_probs_1000, "eng_1000", 1000, eng_1000_alt=eng_mod_1000, eng_1000=eng_words_1000)


        #print(H_trajs["eng_1000"][151])
        #print(H_trajs["eng_1000_alt"][151])
        #print(UID_dev["eng_1000"])
        #print(UID_dev["eng_1000_alt"])
        
	area = calc_UTC(eng_1000_alt=H_trajs["eng_1000_alt"], eng_1000=H_trajs["eng_1000"])
	plot_area(area, "English", 1000)
	mand_reg = UID_dev["eng_1000"]
	mand_alt = UID_dev["eng_1000_alt"]


        plot_mini(H_trajs, "eng_1000")
	
        
	lists = sorted(mand_reg.items())
	lists = [item for item in lists if item[0] % 10 != 0]
	lists1 = sorted(mand_alt.items())
	lists1 = [item for item in lists1 if item[0] % 10 != 0]
	
	x, y = zip(*lists)
	x1, y1 = zip(*lists1)
	
	plt.bar(x1, y1, color="green", label="English alternate", alpha=0.5)
	plt.bar(x, y, color="red", label="English attested", alpha=0.5)
	
	plt.xlabel("Number")
	#plt.xlim(10,100)
	plt.ylabel("UID deviation score")
	plt.legend()
	plt.title("UID deviation")
	plt.savefig("eng1000_num_UID_dev.png")
	plt.gcf().clear()
	print("DONE!!!!!")
