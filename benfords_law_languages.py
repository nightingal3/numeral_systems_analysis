import matplotlib
matplotlib.use("Agg")
import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pickle

def collect_lang_data(filepath):
	# Filepath should be to a directory containing folders labelled with languages
	freq = {}
	for root, dirs, files in os.walk(filepath):
		for d in dirs:
			freq[d] = {}
		
	
	for lang in freq:
		for i in range(10):
			freq[lang][str(i)] = 0
		for s_r, s_d, s_f in os.walk(filepath + "/" + lang):
			for ngram_file in s_f:
				with open(filepath + "/" + lang + "/" + ngram_file, "r") as f:
					for i, line in enumerate(f):
						try:
							freq[lang][line[0][0]] += int(line[2])
						except:
							continue
		print(freq)
	with open("freq.p", "wb") as f:
		pickle.dump(freq, f, protocol=pickle.HIGHEST_PROTOCOL)

	return freq


def plot_languages(langdict, numberline):
	for lang in langdict:
		info = []
		for i in langdict[lang]:
			info.append(langdict[lang][i])
		sum_info = sum(info)
		n_info = [float(i) / (sum(info)) for i in info]
		plt.plot(numberline, n_info, label=lang)
	plt.ylabel("Frequency")
	plt.xlabel("Number line")
	plt.legend()
	plt.xticks(np.arange(numberline[0], numberline[-1] + 1, 1))
	plt.savefig("benford_langs.png")	
	
	return 


if __name__ == "__main__":
	#print(collect_lang_data("downloads/google_ngrams"))
	langdict = pickle.load(open("freq.p", "rb"))
	plot_languages(langdict , [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])		 
