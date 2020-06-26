import matplotlib
matplotlib.use("Agg")
import traceback

import uid

get_need_probs(path):
    """path: directory where probabilities are stored"""
    try:
        eng = open("data/need_probs/eng_num_pos.csv", "r")
         = open("data/need_probs/chn_1_to_1000.csv", "r")
        f_np_all = open("data/need_probs/total_need_prob_num.csv", "rb")
        f_np_mnd = open("data/need_probs/chinese_need_prob.csv", "r")
        f_np_ger = open("data/need_probs/german_need_prob.csv", "r")
        f_np_spa = open("data/need_probs/spanish_need_prob.csv", "r")
        f_np_ita = open("data/need_probs/italian_num_pos.csv", "r")
        f_np_fre = open("data/need_probs/french_need_prob.csv", "r")

    except Exception:
        traceback.print_exc()
        print("At least one file could not be opened. Ensure requisite files are in directory.")

    return {f_np: eng, }
