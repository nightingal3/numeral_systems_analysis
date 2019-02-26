import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def ideal_rig(length, max_info):
    seq = [max_info] + ([0] * length)
    return seq 		


def ideal_uid(length, max_info):
    seq = [0] * (length + 1)
    for i in range(length + 1):
        seq[i] = max_info - (max_info * (i * float(1)/length))
    return seq



if __name__ == "__main__":
    length = 2
    img_dpi = 300
    numberline = [i for i in range(length + 1)]
    ideal_rig = ideal_rig(2, 100)
    ideal_uid = ideal_uid(2, 100)
    print(ideal_rig)
    print(ideal_uid)
    plt.figure(dpi=img_dpi) 
    plt.xlabel("Number of constituents", size=20)
    plt.xticks(numberline, size=18)
    plt.ylabel("Uncertainty", size=20)
    plt.yticks([])
    plt.plot(numberline, ideal_rig, color="blue", label="Ideal RIG profile", linewidth=2)
    plt.plot(numberline, ideal_uid, color="red", linestyle="--", label="Ideal UID profile", linewidth=2)
    plt.legend(prop={"size": 18})
    plt.tight_layout()
    plt.savefig("ideal_rig_uid.eps")
