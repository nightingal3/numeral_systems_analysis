import matplotlib
matplotlib.use("Agg")
from anytree import RenderTree, AsciiStyle
import matplotlib.pyplot as plt

from language_tree import make_tree, calc_complexity, forest_disp, disp
from langstrategy import first_three, successors


def make_rules_up_to_base(base):
    forest = [] 
    if base < 4:  # Handle bases smaller than subitizing range
        for i in range(1, base):
            forest.append(make_tree(i, i, "ONE", True))
        forest.append(make_tree("B", base, "SUC"))
        return forest

    forest = first_three(forest, [1, 2, 3])
    forest = successors(forest, [i for i in range(4, base + 1)], 3, base)

    return forest

def _make_general_rules(base, ulim, forest):
    # TODO: fix this
    num_constituents = div_power(base, ulim)
    forest.append(make_tree(["u", "B"], ["u", str(base)], "MUL"))
    forest.append(make_tree(["v", "w"], ["u", "v"], "ADD"))

    exp = 2
    i = base ** exp
    while i in range(base ** 2, ulim + 1):
        forest.append(make_tree("B" + str(exp), str(exp), [str(base), str(exp)], "POW"))
        exp += 1
        i = base ** exp
    
    constituent_names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in range(3, num_constituents):
        form = constituent_names[:i]
        numexp = constituent_names[:i]
        forest.append(make_tree(form, numexp, "MTA_LONG"))

    for i in range(num_constituents):
        forest.append(make_tree(constituent_names[i] + "_mem", [str(i) for i in range(1, base)], "MEM"))

    return forest


def make_general_rules(base, ulim, forest):
    forest.append(make_tree(["u", "B"], ["u", base], "MUL"))
    forest.append(make_tree(["v", "w"], ["u", "v"], "ADD"))
    
    forest.append(make_tree("u", [i for i in range(2, base) if not is_power_of(base, i * base)], "MEM")) 
    # Generate separate terms for powers of the base  
    exp = 2
    i = base ** exp
    while i in range(base ** 2, ulim + 1):
        forest.append(make_tree("B" + str(exp), str(exp), [str(base), str(exp)], "POW"))
        exp += 1
        i = base ** exp

    # Don't double-count powers of the base   
    bases = set()
    atoms = set()
    for i in range(base, ulim, base):
        for j in range(1, base):
            final_num = i + j
            if not is_power_of(base, final_num):
                bases.add(i)
                atoms.add(j)
    forest.append(make_tree("v", list(bases), "MEM"))
    forest.append(make_tree("w", list(atoms), "MEM"))

    return forest


def is_power_of(base, num):
    if num < base:
        return False
    elif num == base:
        return True
    else:
        return is_power_of(base, num / base)

def div_power(base, num):
    if num < 0:
        raise ValueError
    elif num == 0:
        return 0
    exp = 0
    while base <= num:
        num /= base
        exp += 1
    return exp + 1

def plot_complexities(min_num, max_num, complexities, filename = "base_n_complexities"):
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.plot([i for i in range(min_num, max_num)], complexities, color="#222222")
    plt.xlabel("Base", fontsize=14)
    plt.ylabel("Complexity", fontsize=14)
    plt.xticks([i for i in range(0, max_num, 5)], fontsize=10)
    plt.savefig(filename + ".png")
    plt.savefig(filename + ".eps")


if __name__ == "__main__":
    complexities = [None, 397]  # base 1 doesn't follow same pattern, add empty value so can start at 0
    for base in range(2, 50):
        rules = make_rules_up_to_base(base)
        rules = make_general_rules(base, 1000, rules)
        comp = calc_complexity(rules)
        complexities.append(comp)
    print(enumerate(complexities))

    plot_complexities(0, 50, complexities, filename="complexities_1000")
    
            