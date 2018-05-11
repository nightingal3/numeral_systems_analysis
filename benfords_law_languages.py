import matplotlib
matplotlib.use("Agg")
import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pickle

def collect_lang_data(filepath, dict_name="freq.p", mode=0):
	# Filepath should be to a directory containing folders labelled with languages
	# Modes: 0: numbers 0-9, 1: numbers 10-99, 2: number words
	
	freq = {}
	for root, dirs, files in os.walk(filepath):
		for d in dirs:
			freq[d] = {}
		
	#really ugly
	for lang in freq:
		if mode == 0: 
			for i in range(10):
				freq[lang][str(i)] = 0
		if mode == 1:
			
			for i in range(10, 100):
				freq[lang][str(i)] = 0

		for s_r, s_d, s_f in os.walk(filepath + "/" + lang):
			for ngram_file in s_f:
				with open(filepath + "/" + lang + "/" + ngram_file, "r") as f:
					for i, line in enumerate(f):
						try:
							if mode == 0:
								freq[lang][line[0]] += int(line[2])
							elif mode == 1:
								freq[lang][line[0:2]] += int(line[2])
						except:
							continue
		print(freq)
	with open(dict_name, "wb") as f:
		pickle.dump(freq, f, protocol=pickle.HIGHEST_PROTOCOL)

	return freq


def plot_languages(langdict, mode=0):
	if mode == 0:
		numberline = [i for i in range(10)]
	elif mode == 1:
		numberline = [i for i in range(10, 100)]

	for lang in langdict:
		if lang == "russian": #exclude Russian, dataset is small and noisy
			continue 
		info = []
		if mode == 0:
			for i in range(10):
				info.append(langdict[lang][str(i)])
		elif mode == 1:
			for i in range(10, 100):
				info.append(langdict[lang][str(i)])
		sum_info = sum(info)
		n_info = [float(i) / (sum(info)) for i in info]
		plt.plot(numberline, n_info, label=lang)
	plt.ylabel("Frequency")
	plt.xlabel("Number line")
	plt.legend()
	if mode == 0: #show every tick if only showing first 10 numbers
		plt.xticks(np.arange(numberline[0], numberline[-1] + 1, 1))
	plt.savefig("benford_langs.png")	
	
	return 


if __name__ == "__main__":
	#print(collect_lang_data("downloads/google_ngrams", dict_name="freq2.p", mode=1))
	langdict = pickle.load(open("freq.p", "rb"))
	plot_languages(langdict , mode=0)		 
