import matplotlib
matplotlib.use("Agg")
import csv
import math
import numpy as np
import matplotlib.axes as ax
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pdb


def plot_need_probability(filepath, filepath_fit):
    f = open(filepath, "r")
    f1 = open(filepath_fit, "r")
    numberline = []
    numberline.extend(range(1, 101))

    raw = f.readlines()
    fit = f1.readlines()
    raw_stripped = np.array([s.strip() for s in raw])
    fit_stripped = np.array([s.strip() for s in fit])
    plt.plot([math.log(i) for i in numberline], np.array(
        [math.log(float(i)) for i in raw_stripped]), color="grey", linewidth=2, label="Raw")
    plt.plot([math.log(i) for i in numberline], np.array([math.log(
        float(i)) for i in fit_stripped]), color="black", linewidth=2, label="Smoothed")
    plt.legend(loc="upper right", frameon=False, fontsize=14)

    ax = plt.gca()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.tick_params(axis="both", labelsize=14)

    plt.ylabel("Log frequency", size=16)
    plt.xlabel("Log Number Line", size=16)
    plt.tight_layout()

    plt.savefig("needprobs_log.png")
    plt.savefig("needprobs_log.eps")

    f.close()
    f1.close()


def gen_fitted_need_probs(filepath, coefficient, exp):
    # original fitted line is 0.6182x^-2.02
    y = [coefficient * i ** exp for i in range(1, 101)]
    y = [val / sum(y) for val in y]
    with open(filepath, "w") as np_file:
        writer = csv.writer(np_file)
        for num in y:
            writer.writerow([num])

def gen_fitted_need_probs_log(filepath, coefficient):
    eqn = lambda x: 0.6182 * x - 2.02 * log(0.8)
    y = [eqn(i) for i in range(1, 101)]
    y = [val / sum(y) for val in y]
    return y

def fit_power_law(in_path, out_path):
    base_prob = np.genfromtxt(in_path, delimiter="\n")
    print(base_prob)
    sol1 = curve_fit(func_powerlaw, [i for i in range(1, 101)], base_prob, maxfev=10000, p0=[0.1, 0.1, 0.1])[0]
    fit_vals = func_powerlaw([i for i in range(1, 101)], *sol1)
    fit_vals = [val / sum(fit_vals) for val in fit_vals]
    print(sol1)

def func_powerlaw(x, m, c, c0):
    vals = c0 + x**m * c
    #print(vals)
    #pdb.set_trace()
    if any(v < 0 for v in vals):
        return -np.inf
    return vals
    
if __name__ == "__main__":
    gen_fitted_need_probs("data/need_probs/needprobs_eng_fit_2.csv", 0.6182, -3)
    #plot_need_probability("data/need_probs/need_probs.csv",
                          #"data/need_probs/needprobs_eng_fit.csv")
    #fit_power_law("data/need_probs/need_probs.csv", "data/need_probs/need_probs_power_fit.csv")
