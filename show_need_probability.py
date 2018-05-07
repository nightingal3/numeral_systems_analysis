import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np

def plot_need_probability(filepath, filepath_fit):
	f = open(filepath, "r")
	f1 = open(filepath_fit, "r")
	numberline = []
	numberline.extend(range(1, 101))
	raw = f.readlines()
	fit = f.readlines()
	raw_stripped = [s.strip() for s in raw]
	fit_stripped = [s.strip() for s in fit]
	print([float(i) for i in raw_stripped])
	plt.plot(numberline, [float(i) for i in raw_stripped], color="grey", linewidth=2)
	plt.plot(numberline, [float(i) for i in fit_stripped], color="black", linewidth=2)
	plt.yscale("log")
	plt.ylabel("Log probability")
	plt.xlabel("Number line")
	plt.savefig("needprobs.png")


if __name__ == "__main__":
	plot_need_probability("data/need_probs/need_probs.csv", "data/need_probs/needprobs_eng_fit.csv")
 
