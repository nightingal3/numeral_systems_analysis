from routines.get_term_num_matrix import get_term_num_matrix, get_num_term_pt
from routines.compute_P_w_i_bias_correct_subitized import compute_P_w_i_bias_correct_subitized, compute_P_w_i_bias_correct, compute_P_w_i_size_principle
import math
import itertools
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use("Agg")
sys.path.insert(0, "routines")
plt.style.use("seaborn-colorblind")


def show_munduruku_fit(percent_file, terms_file, term_interp_file, model="subitize"):
    # Data is from Pica(2004)
    subrange = [1, 2, 3]
    mu_range = []
    mu_range.extend(range(1, 16))
    w = 0.31
    c = 1 / (math.sqrt(2)*w)

    numberline = mu_range
    percent = np.loadtxt(open(percent_file, "rb"),
                         delimiter=",").astype("float")
    terms = np.loadtxt(open(terms_file, "rb"), delimiter=",", dtype="string")
    term_interp = np.loadtxt(open(term_interp_file, "rb"),
                             delimiter=",", dtype="string")
    nnum, ncat = 15, terms.shape[0]

    bias = 55 * percent
    bias = np.sum(bias, axis=1)
    bias = bias / np.sum(bias)

    total_mass = np.sum(percent, axis=0)
    total_mass[1:4] = 1

    mu_placements = np.array(list((itertools.combinations(mu_range, ncat))))
    n_placements = mu_placements.shape[0]

    # Plot Munduruku data
    colors = itertools.cycle(["r", "g", "b", "c", "m", "y", "k", "#e89600"])
    title0 = itertools.cycle(terms)
    title1 = itertools.cycle(term_interp)

    fig, (ax_data, ax_model) = plt.subplots(1, 2, sharey=False)
    for row in percent:
        ax_data.plot(numberline, row, next(colors),
                     label=next(title0) + "=" + next(title1))

    # Plot model data
    P_w_i_opt = None
    min_mse = float("inf")
    mu_opt = None
    for i in range(n_placements):
        mus = mu_placements[i, :]
        if model == "subitize":
            P_w_i = compute_P_w_i_bias_correct_subitized(
                nnum, ncat, mus, c, w, total_mass, subrange, bias
			)
        elif model == "no_subitize":
            P_w_i = compute_P_w_i_bias_correct(
                nnum, ncat, mus, c, w, total_mass, bias)
        elif model == "size_principle":
            num_term_pt = get_num_term_pt(numberline, list(mus))
            term_num_matrix = get_term_num_matrix(
                mus, nnum, num_term_pt, 0, numberline)
            P_w_i = compute_P_w_i_size_principle(term_num_matrix)

        mse_curr = np.mean(
            np.mean((P_w_i[:, :percent.shape[1]] - percent) ** 2, axis=1))
        if mse_curr < min_mse:
            min_mse = mse_curr
            P_w_i_opt = P_w_i
            mu_opt = mus

    print("MSE:" + str(min_mse))

    for row in P_w_i_opt:
        ax_model.plot(numberline, row, next(colors))

    handles, labels = ax_data.get_legend_handles_labels()
    lgd = fig.legend(handles, labels, loc="center right",
                     bbox_to_anchor=(1.28, 0.5), prop={"size": 8})
    ax_data.set_xlabel("Number line")
    ax_model.set_xlabel("Number line")
    ax_data.spines["right"].set_visible(False)
    ax_data.spines["top"].set_visible(False)
    ax_model.spines["right"].set_visible(False)
    ax_model.spines["top"].set_visible(False)
    ax_data.set_ylabel("Response frequency")
    lab_a = ax_data.text(-0.13, 1.1, "A", transform=ax_data.transAxes,
                         fontsize=14, fontweight="bold", va="top", ha="right")
    lab_b = ax_model.set_ylabel("P(w|i)")
    ax_model.text(-0.13, 1.1, "B", transform=ax_model.transAxes,
                  fontsize=14, fontweight="bold", va="top", ha="right")

    ax_data.set_title("Empirical data")
    ax_model.set_title("Model fit")
    ax_data.set_yticks([0.1 * x for x in range(0, 11)])
    ax_data.set_ybound((0, 1))
    ax_model.set_yticks([0.1 * x for x in range(0, 11)])
    ax_model.set_ybound((0, 1))
    plt.tight_layout()
    plt.savefig("mund_comp_nosub.png", dpi=1000, bbox_extra_artists=(
        lgd, lab_a, lab_b), bbox_inches="tight")
    plt.savefig("mund_comp_nosub.eps", dpi=1000, bbox_extra_artists=(
        lgd, lab_a, lab_b), bbox_inches="tight")
    


if __name__ == "__main__":
    show_munduruku_fit("data/munduruku_pica2004/percent.csv", "data/munduruku_pica2004/terms.csv",
                       "data/munduruku_pica2004/term_interp.csv", model="no_subitize")
