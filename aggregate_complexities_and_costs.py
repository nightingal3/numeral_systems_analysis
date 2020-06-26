import numpy as np
import math
import pickle
import os
import inspect
from collections import defaultdict

from itertools import chain
from timeit import default_timer as timer
from scipy.spatial import ConvexHull
import matplotlib
matplotlib.use("Agg")
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon, Patch
import matplotlib.pyplot as plt


from routines.find import *
from routines.compute_base_n_complexities import *
from routines import compute_cost, test_gauss_blob_place_mu_greedy
import langstrategy
import language_tree
from config import *
import pdb


def aggregate_complexities():
    """ Aggregates the complexities for attested languages."""

    info = {}

    # assume naming convention is respected...
    langlist = [i[0] for i in inspect.getmembers(
        langstrategy, inspect.isfunction) if len(i[0]) == 3]

    for i in range(len(langlist)):
        complexity, num_type, ulim = language_tree.build_language(
            langlist[i], stored_info="language_data.p", save=True)
        info[langlist[i]] = (complexity, num_type)

    return info


def aggregate_communicative_costs(need_probs, lang_info, dict_name="attested.p", w=0.31):
    """ Aggregates the communicative costs for attested languages.
    lang_info should be a dict organized as {lang:(comp, num_type)}"""

    langs = lang_info.keys()
    complexities = [i[1][0] for i in lang_info.items()]
    lang_by_category = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    term = {"prh": ["hoi_1", "hoi_2", "aibaagi"], "war": ["xica pe", "dois"], "goo": [
        "yoowarni", "garndiwiddidi", "ngarloodoo", "marla"], "myu": ["pug", "xep xep", "ebapug", "ebadipdip", "adesu", "ade"], 
        "chi": ["taman", "surumana"], "fuy": ["fidan", "yovalo", "yovalo hul mindan",  "hukas"],
        "knk": ["putchik", "narimbo", "krutuip", "inhauit"]}
    num_term_pt = {"prh": [1, 2, 2, 2, 3, 3, 3, 3, 3, 3], "war": [
        1, 2], "goo": [1, 2, 3, 3, 4], "myu": [1, 2, 3, 4] + [5] * 7, "chi": [1], "fuy": [1, 2, 3], "knk": [1, 2, 3]}
    end_category = {"prh": 0, "war": 0, "goo": 0, "myu": 0, "chi": 0, "fuy": 0, "knk": 0}
    numberline = [i for i in range(1, 101)]
    for item in lang_info.items():
        lang_by_category[item[1][1]].append(item[0])
    costs = {}
    ulim = {}

    # Restricted approximate systems
    for lang in lang_by_category[0]:
        costs[lang] = compute_cost.compute_approx_cost(
            term[lang], numberline, num_term_pt[lang], end_category[lang], need_probs, w=w)

    # Restricted exact systems
    for lang in lang_by_category[1]:
        ulim[lang] = language_tree.build_language(lang)[2]
        costs[lang] = compute_cost.compute_cost_size_principle(
            ulim[lang], need_probs)

    ret = {}
    for lang in costs:  # return as (complexity, cost, lang_type)
        ret[lang] = (lang_info[lang][0], costs[lang], lang_info[lang][1])

    pickle.dump(ret, open(dict_name, "wb"))

    return ret


def generate_hypothetical_systems(numberline, c, w, need_probs, stored_data_dir=None, write=True):
    """ Generates hypothetically possible numeral systems (approximate and exact restricted)
    Approximate systems are generated randomly, but only the most efficient and least efficient (for typical need distribution) restricted systems are generated.
    """
    if stored_data_dir:
        try:
            comp_rand = pickle.load(
                open(stored_data_dir + "/comp_rand.p", "rb"))
            cost_rand = pickle.load(
                open(stored_data_dir + "/cost_rand.p", "rb"))
            compfenew = pickle.load(
                open(stored_data_dir + "/compfenew.p", "rb"))
            costfenew = pickle.load(
                open(stored_data_dir + "/costfenew.p", "rb"))
            compfe1new = pickle.load(
                open(stored_data_dir + "/compfe1new.p", "rb"))
            costfe1new = pickle.load(
                open(stored_data_dir + "/costfe1new.p", "rb"))
            base_n_complexity = pickle.load(
                open(stored_data_dir + "/base_n_complexity.p", "rb"))

            try:
                close(stored_data_dir + "/comp_rand.p")
                close(stored_data_dir + "/cost_rand.p")
                close(stored_data_dir + "/compfe1new.p")
                close(stored_data_dir + "/costfe1new.p")
                close(stored_data_dir + "/base_n_complexity.p")
            except:
                print("Files could not be closed")

            return comp_rand, cost_rand, compfenew, costfenew, compfe1new, costfe1new, base_n_complexity
        except:
            print("Please enter valid directory that hypothetical data was written to")
            return

    nitr = 100
    numterms = [i for i in range(2, 56)]
    numterms_2 = [i for i in range(2, 52)]
    complexperm_rand = []
    costperm_rand = []
    mus_best_rand = []
    mus_worst_rand = []
    comp_rand = []
    cost_rand = []

    # Approximate systems
    for t in range(len(numterms)):
        comp_lower_bound, cost_lower_bound, mus_min, term_map_min = test_gauss_blob_place_mu_greedy(len(
            numberline), numterms[t], numberline, [i for i in range(max(numberline))], c, w, need_probs, nitr, -1)
        comp_upper_bound, cost_upper_bound, mus_max, term_num_max = test_gauss_blob_place_mu_greedy(len(
            numberline), numterms[t], numberline, [i for i in range(max(numberline))], c, w, need_probs, nitr, 1)

        cost_lower_bound.extend(cost_upper_bound)
        comp_lower_bound.extend(comp_upper_bound)
        costperm_rand.append(cost_lower_bound)
        complexperm_rand.append(comp_lower_bound)
        mus_best_rand.append(mus_min)
        mus_worst_rand.append(mus_max)

    comp_rand, cost_rand = reconfig_comp_cost(complexperm_rand, costperm_rand)
    
    compfenew = [0] * len(numterms_2)
    costfenew = [0] * len(numterms_2)
    # Exact restricted systems
    for i in range(len(numterms_2)):
        if i <= len(numterms_2):
            tn = numterms_2[i] - 1
        else:
            tn = i
        if tn <= 3:
            compfenew[i] = tn * 3 + 4
        else:
            compfenew[i] = 3*3 + (tn - 3) * 4 + 4
        costfenew[i] = compute_cost.compute_cost_size_principle(tn, need_probs)

    compfe1new = [0] * len(numterms_2)
    costfe1new = [0] * len(numterms_2)

    nnum = len(numberline)
    for i in range(len(numterms_2)):
        ncats = numterms_2[i]
        if ncats > 4:
            modemap = [1, 2, 3]
            modemap.extend([4] * (nnum - 3))
            basen = 5
            modemap[-(ncats - 4):] = [n for n in range(basen,
                                                       basen + (ncats - 5) + 1)]
            compfe1new[i] = 3*3 + 4*(ncats - 3)
        elif ncats == 4:
            modemap = [1, 2, 3]
            modemap.extend([4] * (nnum - 3))
            compfe1new[i] = 3*3 + 4*(ncats - 3)
        elif ncats == 3:
            modemap = [1, 2]
            modemap.extend([3] * (nnum - 2))
            compfe1new[i] = 3*2 + 4*(ncats - 2)
        elif ncats == 2:
            modemap = [1]
            modemap.extend([2] * (nnum - 1))
            compfe1new[i] = 3 + 4*(ncats - 1)

        costfe1new[i] = compute_cost.compute_cost_size_principle_arb(
            modemap[::-1], need_probs)

    # recursive systems
    #min_recursive, max_recursive = compute_base_n_complexities()
    min_recursive, max_recursive = [48, 399]
    base_n_complexity = [min_recursive, max_recursive]

    if write:
        if not os.path.isdir("hyp_lang_data"):
            os.mkdir("hyp_lang_data")
        pickle.dump(cost_rand, open("hyp_lang_data/cost_rand.p", "wb"))
        pickle.dump(comp_rand, open("hyp_lang_data/comp_rand.p", "wb"))
        pickle.dump(compfenew, open("hyp_lang_data/compfenew.p", "wb"))
        pickle.dump(costfenew, open("hyp_lang_data/costfenew.p", "wb"))
        pickle.dump(compfe1new, open("hyp_lang_data/compfe1new.p", "wb"))
        pickle.dump(costfe1new, open("hyp_lang_data/costfe1new.p", "wb"))
        pickle.dump(base_n_complexity, open(
            "hyp_lang_data/base_n_complexity.p", "wb"))

    return comp_rand, cost_rand, compfenew, costfenew, compfe1new, costfe1new, base_n_complexity


def plot_cost_vs_complexity(lang_info, hyp_lang_info, filename, dist_type="normal", w=0.31, plot_inefficient=False):
    """ Plots cost against complexity for both attested and hypothetical systems."""
    fig, ax = plt.subplots()

    # attested languages
    langcode_to_name = {"ana": "Araona$^1$", "awp": "Awa Pit$^2$", "ram": "Rama$^3$", "war": "Wari", "prh": "Piraha", "goo": "Gooniyandi", "wch": "Wichi",
                        "wsk": "Waskia", "hpd": "Hup", "mnd": "Mandarin", "ain": "Ainu", "eng": "English", "geo": "Georgian", "myu": "Munduruku",
                        "chi": "Chiquitano", "fuy": "Fuyuge", "knk": "Krenák", "spa": "Spanish", "fre": "French"}
    colorscheme = {1: "green", 6: "blue", 5: "blue", 0: "red"}

    if dist_type == "uniform":
        offsets = {"war": (-5, 2), "prh": (0, 1), "goo": (5, 0), "geo": (0, -2), "eng": (-15, -2), "ain": (0, -2), "geo": (
            0, -2), "mnd": (-0.02, -2), "wsk": (0, 1), "ana": (-5, 1), "awp": (-0.5, 3), "myu": (3, 0), "chi": (-18, 2), "fuy": (0, 2), "myi": (5, 0), "ram": (5, 0),
            "knk":(0, -3), "fre": (5, 3), "spa": (-15, 3)}  # sadly must be done
    elif dist_type == "steep":
        offsets = {"war": (0, 0.05), "prh": (5, 0), "goo": (5, 0.1), "geo": (0, -0.2), "eng": (-15, -0.1), "ain": (0.2, -0.1), "geo": (
            0, -0.1), "mnd": (0, -0.1), "wsk": (0, 0.07), "ana": (3, 0.1), "awp": (-5, -0.1), "myu": (14, 0.05), "fre": (5, 0.1), "spa": (-15, 0.1),
            "ram": (5, -1), "ana": (-20, -0.5), "knk": (0, 0.05), "chi": (5, 0), "fuy": (-3, 0.1)}
    elif w == 0.15:
        offsets = {"war": (0, 0.5), "prh": (5, 0.02), "goo": (-17, -1), "geo": (0, -2), "eng": (-15, -2), "ain": (0, -2), "geo": (
            0, -2), "mnd": (0, -2), "wsk": (0, 0.5), "ana": (-13, 0), "awp": (-3, -1), "myu": (5, 0), "fre": (5, 0.5), "spa": (-15, 0.5),
            "fuy": (5, 0), "knk": (0, 0.75), "ram": (0, -0.5), "chi": (-1, -1.5), "hpd": (0, 0.5), "wch": (0, 0.5)}  # sadly must be done
    elif w == 0.25:
        offsets = {"war": (0, 0.15), "prh": (5, 0.02), "goo": (-27, -0.25), "geo": (0, -0.2), "eng": (-15, -0.5), "ain": (0, -0.5), "geo": (
            0, -0.5), "mnd": (0, -0.5), "wsk": (0, 0.07), "ana": (-20, -0.5), "awp": (-15, -0.35), "myu": (5, 0),
            "hpd": (0, 0.25), "wch": (0, 0.25), "ram": (3, -1.25), "chi": (5, 0), "knk": (0, 0.15), "spa": (-15, 0.25), "fre": (5, 0.25),
            "fuy": (5, 0)}  # sadly must be done
    else:
        offsets = {"war": (0, 0.15), "prh": (5, -0.1), "goo": (-27, 0), "eng": (-15, -0.5), "ain": (0, -0.5), "geo": (
            0, -0.5), "mnd": (-0.25, 0.25), "wsk": (0, 0.25), "ana": (-15, -0.35), "awp": (-5, -0.55), "myu": (5, 0),
            "chi": (0, 0.15), "spa": (-10, 0.25), "knk": (5, 0), "ram": (5, -1.15), "hpd": (0, 0.1), "fuy": (0, 0.2),
            "mnd": (0, -0.25), "hpd": (0, 0.25), "fre": (5, 0.45), "wch": (5, -0.15)}  # sadly must be done

    seen = {}
    for lang in lang_info:
        x_offset = 5
        y_offset = 0.05
        if lang in offsets:
            x_offset = offsets[lang][0]
            y_offset = offsets[lang][1]
        else:
            x_offset = 0
            y_offset = 0
        if (lang_info[lang][0], lang_info[lang][1]) not in seen:
            seen[(lang_info[lang][0], lang_info[lang][1])] = 1
        else:
            y_offset += 0.5 * seen[(lang_info[lang][0], lang_info[lang][1])]
            seen[(lang_info[lang][0], lang_info[lang][1])] += 1


        ax.plot([lang_info[lang][0]], [lang_info[lang][1]], marker='o', color=colorscheme[lang_info[lang]
                                                                                              [2]], markersize=7, markerfacecolor="none", linewidth=3, zorder=999)
        if lang in langcode_to_name:                                                                              
            ax.annotate(langcode_to_name[lang], (lang_info[lang][0] +
                                                x_offset, lang_info[lang][1] + y_offset), size=7, zorder=999)

    # hypothetical languages
    comp_rand, cost_rand, compfenew, costfenew, compfe1new, costfe1new, base_n_complexity = hyp_lang_info
    comp_rand_new = []
    cost_rand_new = []
    minmin = 999
    maxmax = 0
    for n in range(len(comp_rand)):
        minv = min(cost_rand[n])
        maxv = max(cost_rand[n])
        if minv < minmin:
            minmin = minv
        if maxv > maxmax:
            maxmax = maxv
        if minv is not None and maxv is not None:
            comp_rand_new.extend([comp_rand[n], comp_rand[n]])
            cost_rand_new.extend([minv, maxv])

    assert len(comp_rand_new) == len(cost_rand_new)
    compfenew.extend(compfe1new)
    costfenew.extend(costfe1new)
    
    # plot actual points
    plt.scatter(compfenew, costfenew, color="#CDCFD3", s=2)
    plt.scatter(comp_rand_new, cost_rand_new, color="#676768", s=2)

    # sampled inefficient points
    if plot_inefficient:
        inefficient = [(11, 3.88, "A1"), (16, 3.65, "A2"), (20, 3.72, "A3"), (24, 3.61, "A4"),
        (17, 8.21, "E1"), (21, 6.56, "E2"), (25, 5.88, "E3"), (29, 5.51, "E4")]
        plt.scatter([11, 16, 20, 24], [3.88, 3.65, 3.72, 3.61], color="#fc03a9", s=3)
        plt.scatter([17, 21, 25, 29], [8.21, 6.56, 5.88, 5.51], color="#fc03a9", s=3)

        offsets = {"A1": (0, 0), "A2": (-7, -0.35), "A4": (4, -0.25), "A3": (2, 0.15)}
        for pt in inefficient:
            coord = (pt[0] + offsets[pt[2]][0], pt[1] + offsets[pt[2]][1]) if pt[2] in offsets else (pt[0] + 5, pt[1] + 0.15)
            ax.annotate(pt[2], coord, size=7)
    
    exact_points = np.transpose(np.array((compfenew, costfenew)))
    approx_points = np.transpose(np.array((comp_rand_new, cost_rand_new)))
    #plt.plot(exact_points[:, 0], exact_points[:, 1])
    #plt.plot(approx_points[:, 0], approx_points[:, 1])

    hull_exact = ConvexHull(exact_points)
    hull_approx = ConvexHull(approx_points)

    for simplex in hull_exact.simplices:
        plt.plot(exact_points[simplex, 0],
                 exact_points[simplex, 1], color="#CDCFD3")
    for simplex in hull_approx.simplices:
        plt.plot(approx_points[simplex, 0],
                 approx_points[simplex, 1], color="#676768")
    plt.fill(approx_points[hull_approx.vertices, 0],
             approx_points[hull_approx.vertices, 1], alpha=0.3, color="#676768")
    plt.fill(exact_points[hull_exact.vertices, 0],
             exact_points[hull_exact.vertices, 1], alpha=0.3, color="#CDCFD3")

    plt.plot([base_n_complexity[0], base_n_complexity[1]],
             [0, 0], label="Hypothetical (Recursive)")

    plt.xlabel("Complexity", fontsize="x-large")
    plt.ylabel("Communicative cost", fontsize="x-large")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    legend_elements = [
        Line2D([0], [0], marker="o", color="r", lw=0,
               markerfacecolor="none", label="Approximate"),
        Line2D([0], [0], marker="o", color="g", lw=0,
               markerfacecolor="none", label="Exact restricted"),
        Line2D([0], [0], marker="o", color="b", lw=0,
               markerfacecolor="none", label="Recursive"),
        Line2D([0], [0], color="b", lw=2, label="Hypothetical (Recursive)"),
        Patch(facecolor="#888889", edgecolor="#676768",
              label="Hypothetical (Approx.)"),
        Patch(facecolor="#e8e9ea", edgecolor="#CDCFD3",
              label="Hypothetical (Exact restr.)")
    ]
    if plot_inefficient:
        legend_elements.insert(3, Line2D([0], [0], marker=".", color="#fc03a9", lw=0,
               markerfacecolor="#fc03a9", label="Hypothetical inefficient"))

    plt.legend(handles=legend_elements, loc="upper right", prop={"size": 8})
    plt.xlim(xmax=200)

    if w == 0.15:
        plt.ylim(ymax=24, ymin=-3)
    elif w == 0.25:
        plt.ylim(ymax=7, ymin=-2)
    elif dist_type == "uniform":
        plt.ylim(ymax=50)
    elif dist_type == "steep":
        plt.ylim(ymax=2)
    else:
        plt.ylim(ymax=9)
    #ax.set_rasterized(True)

    plt.savefig(filename + ".png", dpi=1000)
    plt.savefig(filename + ".eps", dpi=500)
    plt.savefig(filename + ".pdf")
    plt.gcf().clear()
    return


def reconfig_comp_cost(comp_m, cost_m):
    unique = find_unique(comp_m[0])
    for i in range(1, len(comp_m)):
        unique.extend(comp_m[i])

    unique = find_unique(unique)
    nc = len(unique)
    cost = []
    for i in range(nc):
        cost.append([])
        for j in range(len(cost_m)):
            inds = find(comp_m[j], unique[i])
            if len(inds) != 0:
                for ind in inds:
                    cost[i].append(cost_m[j][ind])

        zinds = find(cost[i], float("inf"))
        cost[i] = [val for index, val in enumerate(
            cost[i]) if index not in zinds]

    return unique, cost


def main():
    c = aggregate_complexities()
    f = open("data/need_probs/needprobs_eng_fit.csv")
    f1 = open("data/need_probs/needprobs_eng_fit_2.csv")

    need_probs = [float(i) for i in f.read().split("\n")[:-1]]
    need_probs_uniform = [float(1)/100 for i in range(0, 100)]
    need_probs_steeper = [float(i) for i in f1.read().split("\n")[:-1]]
    
    aggregate_communicative_costs(need_probs_uniform, c, "attested_bayesian_ext_03.p", w=0.31)
    y = generate_hypothetical_systems(
        [i for i in range(1, 101)], 2.28, 0.31, need_probs_uniform)
    pickle.dump(y, open("hypothetical_systems_03.p", "wb"))

    f1 = open("attested_bayesian_ext_03.p", "rb")
    x = pickle.load(f1)
    y = pickle.load(open("hypothetical_systems_03.p", "rb"))

    x["eng"] = (117, 0, 6)
    x["mnd"] = (73, 0, 6)
    x["geo"] = (153, 0, 6)
    x["ain"] = (121, 0, 6)
    x["fre"] = (123, 0, 5)
    x["spa"] = (118, 0, 6)

    plot_cost_vs_complexity(x, y, "cvc_flat_new", w=0.31, dist_type="uniform", plot_inefficient=False)
    f.close()


if __name__ == "__main__":
    main()