import matplotlib.pyplot as plt
import math
import matplotlib
matplotlib.use("Agg")


def compute_base_n_complexities(plot=0):
    # 2 - 11
    c = [397, 208, 127, 98, 104, 116, 106, 113, 92, 94]

    # 12 - 49
    bs = [i for i in range(12, 50)]
    a = [0] * (len(bs))
    for i in range(len(bs)):
        b = bs[i]
        x = math.floor(100/b) - 1 + 2
        a[i] = 3*3 + (b - 1) * 4 + x + 16 + (x + 1) + (2 + b - 1)
    c.extend(a)

    # 50 - 100
    bs = [i for i in range(50, 101)]
    a = [0] * (len(bs))
    for i in range(len(bs)):
        b = bs[i]
        a[i] = 3*3 + (b - 1) * 4 + ((100-b) + 2 + 8) * (b < 100)

    c.extend(a)

    min_c = min(c)
    max_c = max(c)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    if plt:
        plt.plot([i for i in range(2, 51)], c[:49], color="#222222")
        plt.xlabel("Base", fontsize=14)
        plt.ylabel("Complexity", fontsize=14)
        plt.xticks([i for i in range(0, 55, 5)], fontsize=10)
        plt.savefig("base_complexities.eps")

    return min_c, max_c


if __name__ == "__main__":
    print(compute_base_n_complexities(plot=1))
