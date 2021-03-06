import matplotlib
matplotlib.use("Agg")
from anytree import RenderTree, AsciiStyle
import matplotlib.pyplot as plt

from language_tree import make_tree, calc_complexity, forest_disp, disp
from langstrategy import first_three, successors
import pdb

def make_rules_up_to_base(base: int):
    forest = [] 
    if base < 4:  # Handle bases smaller than subitizing range
        for i in range(1, base):
            forest.append(make_tree(i, i, "ONE", True))
        forest.append(make_tree("B", base, "SUC"))
        return forest

    forest = first_three(forest, [1, 2, 3])
    forest = successors(forest, [i for i in range(4, base + 1)], 3, base)

    return forest

def make_general_rules_(base: int, ulim: int, forest: list):
    forest.append(make_tree(["u", "B"], ["u", base], "MUL"))
    forest.append(make_tree(["v", "w"], ["u", "v"], "ADD"))

    #if base == 10:
        #pdb.set_trace()
    if base ** 2 <= ulim:
        forest.append(make_tree("u", range(2, (ulim + 1) // base), "MEM")) 
    else:
        forest.append(make_tree("u", range(2, base), "MEM"))
    #forest.append(make_tree("B^n", [str(base), "n"], "POW"))
    # Generate separate terms for powers of the base  
    exp = 2
    i = base ** exp
    powers = []
    while i in range(base ** 2, ulim + 1):
        forest.append(make_tree("B**" + str(exp), [str(base), str(exp)], "POW"))
        powers.append(i)
        exp += 1
        i = base ** exp

    forest.append(make_tree("powers", powers, "MEM"))

    # Don't double-count powers of the base   
    bases = set()
    atoms = set()
    for i in range(base, ulim + 1, base):
        for j in range(1, base):
            final_num = i + j
            if not is_power_of(base, final_num):
                bases.add(i // base)
                atoms.add(j)
    bases.remove(1)
    forest.append(make_tree("v", list(bases), "MEM"))
    forest.append(make_tree("w", list(atoms), "MEM"))

    return forest

def make_general_rules(base: int, ulim: int, forest: list):
    forest.append(make_tree(["d", "P"], ["d", "P"], "MUL"))
    forest.append(make_tree(["M", "N"], ["M", "N"], "ADD"))

    forest.append(make_tree("digits", range(1, base), "MEM"))
    # Generate separate terms for powers of the base  
    exp = 2
    i = base ** exp
    powers = []
    while i in range(base ** 2, ulim + 1):
        forest.append(make_tree("B**" + str(exp), [str(base), str(exp)], "POW"))
        powers.append(i)
        exp += 1
        i = base ** exp

    powers.append(base)

    """for p in powers:
        mult = []
        for i in range(1, base):
            if i * p >= ulim:
                break
            mult.append(i * p)
        forest.append(make_tree("power " + str(p), mult, "MEM"))"""

    forest.append(make_tree("powers", powers, "MEM"))

    return forest


def is_power_of(base: int, num: int):
    if num < base:
        return False
    elif num == base:
        return True
    else:
        return is_power_of(base, num / base)

def div_power(base: int, num: int):
    if num < 0:
        raise ValueError
    elif num == 0:
        return 0
    exp = 0
    while base <= num:
        num /= base
        exp += 1
    return exp + 1

def plot_complexities(min_num: int, max_num: int, complexities: list, filename: str = "base_n_complexities"):
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
    complexities = [None, 99 * 4 + 3]  # base 1 doesn't follow same pattern, add empty value so can start at 0
    for base in range(2, 50):
        rules = make_rules_up_to_base(base)
        rules = make_general_rules(base, 100, rules)
        if base == 5:
            print("== Base {} ==".format(base))
            for rule in rules:
                print(RenderTree(rule, style=AsciiStyle()))
        comp = calc_complexity(rules)
        complexities.append(comp)

    print(complexities)

    plot_complexities(0, 50, complexities, filename="complexities_100")
    