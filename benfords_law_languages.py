import matplotlib
matplotlib.use("Agg")
import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pickle

def collect_lang_data(filepath, dict_name="freq.p", mode=0, decades="all"):
	# Filepath should be to a directory containing folders labelled with languages
	# Modes: 0: numbers 0-9, 1: numbers 10-99, 2: number words
	# decades: [decade1, decade2], e.g. [1800, 1920]
	
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
                                                line = line.split('\t')
						try:
							if mode == 0:
                                                                if decades == "all":
                                                                        freq[lang][line[0][0]] += int(line[2])
                                                                else:
                                                                        if int(line[1]) in range(decades[0], decades[1]):
                                                                                freq[lang][line[0][0]] += int(line[2])
							elif mode == 1:
                                                                if decades == "all":
                                                                        freq[lang][line[0][0:2]] += int(line[2])
                                                                else:
                                                                        if int(line[1]) in range(decades[0], decades[1]):
                                                                                freq[lang][line[0][0:2]] += int(line[2])
						except:
							continue
		print(freq)
	with open(dict_name, "wb") as f:
		pickle.dump(freq, f, protocol=pickle.HIGHEST_PROTOCOL)

	return freq


def plot_languages(langdict, mode=0, filename="benford_langs.png"):
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
	plt.savefig(filename)	
	
	return 


if __name__ == "__main__":
	collect_lang_data("downloads/google_ngrams", dict_name="freq.p", mode=1, decade=[1800, 1850])
        collect_lang_data("downloads/google_ngrams", dict_name="freq2.p", mode=1, decade=[1850, 1900])
        collect_lang_data("downloads/google_ngrams", dict_name="freq3.p", mode=1, decade=[1900, 1950]) 
	langdict = pickle.load(open("freq.p", "rb"))
	ld2 = pickle.load(open("freq2.p", "rb"))
	ld3 = pickle.load(open("freq3.p", "rb"))
	plot_languages(langdict , mode=1, filename="1800to1850.png")		 
	plot_languages(ld2, mode=1, filename="1850to1900.png")
	plot_languages(ld3, mode=1, filename="1900to1950.png")	
