import argparse
import csv
import math
import numpy as np
import matplotlib.axes as ax
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


def plot_need_probability(filepath, filepath_fit, filename="need_probs_plot"):
    f = open(filepath, "r")
    f1 = open(filepath_fit, "r")
    numberline = []
    numberline.extend(range(1, 101))

    raw = f.readlines()
    fit = f1.readlines()
    raw_stripped = np.array([s.strip() for s in raw])
    fit_stripped = np.array([s.strip() for s in fit])
    plt.plot(numberline, np.array(
        [math.log(float(i)) for i in raw_stripped]), color="grey", linewidth=2, label="Raw")
    plt.plot(numberline, np.array([math.log(
        float(i)) for i in fit_stripped]), color="black", linewidth=2, label="Smoothed")
    plt.legend(loc="upper right", frameon=False, fontsize=14)

    ax = plt.gca()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.tick_params(axis="both", labelsize=14)

    plt.ylabel("Log frequency", size=16)
    plt.xlabel("Number", size=16)
    plt.savefig(filename + ".png")
    plt.savefig(filename + ".eps")

    f.close()
    f1.close()


def gen_fitted_need_probs(filepath, coefficient, exp):
    # original fitted line is 0.6182x^-2.02
    y = [coefficient * i ** exp for i in range(1, 101)]
    y = [num / sum(y) for num in y]
    with open(filepath, "w") as np_file:
        writer = csv.writer(np_file)
        for num in y:
            writer.writerow([num])


if __name__ == "__main__":
    gen_fitted_need_probs("data/need_probs/needprobs_eng_fit_1.csv", 0.6182, -3)
    plot_need_probability("data/need_probs/need_probs.csv",
                          "data/need_probs/needprobs_eng_fit.csv")
