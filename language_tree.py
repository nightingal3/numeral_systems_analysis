from anytree import Node, RenderTree, LevelOrderIter
from anytree.dotexport import RenderTreeGraph
from anytree.exporter import DotExporter
import os
import inspect
import pickle
import langstrategy
import sys
import pdb


def make_tree(form, numexp, op, numeral_only=False):
    """Makes a tree for the given expression, where the left subtree represents the form and the right subtree represents the expression."""
    root = Node("=")

    # construct the tree according to the setting given.
    if op == "MEM":
        root = Node(form)
        in_set = Node(u'\u2208', parent=root)
        names = [i for i, f in enumerate(numexp)]
        for i in range(len(names)):
            names[i] = Node(numexp[i], parent=in_set)

    elif op == "ONE" or op == "EQU":
        if op == "EQV":
            root = Node(u'\u2263')
        if not numeral_only:
            l = Node(form, parent=root)
        r = Node(numexp, parent=root)

    elif op == "GAU":
        if not numeral_only:
            l = Node(form, parent=root)
        r_root = Node("g" + str(numexp), parent=root)

    elif op == "SUC":
        if not numeral_only:
            l = Node(form, parent=root)
        r_root = Node("s", parent=root)
        r_exp = Node(numexp - 1, parent=r_root)

    elif op == "HIG":
        if not numeral_only:
            l = Node(form, parent=root)
        r = Node(">", parent=root)
        r_c = Node(str(numexp[0]), parent=r)

    elif op in ["ADD", "SUB", "MUL", "DIV", "POW"]:
        if (isinstance(form, list) and len(form) == 3) and not numeral_only:
            l_root = Node(form[1], parent=root)
            l_l = Node(form[0], parent=l_root)
            l_r = Node(form[2], parent=l_root)
        elif (isinstance(form, list) and len(form) > 3) and not numeral_only:
            # not sure how to represent this linguistically, just put all the components on the left
            names = [i for i, f in enumerate(form)]
            for i in range(len(form)):
                names[i] = Node(form[i], parent=root)
        elif isinstance(form, list) and not numeral_only:
            l_root = Node(form[0], parent=root)
            l_c = Node(form[1], parent=l_root)
        elif not numeral_only:
            l_root = Node(form, parent=root)

        if op == "ADD":
            r_root = Node("+", parent=root)
        elif op == "SUB":
            r_root = Node("-", parent=root)
        elif op == "MUL":
            r_root = Node(u'\u2715'.encode("utf-8"), parent=root)
        elif op == "DIV":
            r_root = Node(u'\u00f7', parent=root)
        elif op == "POW":
            r_root = Node(u'\u2191', parent=root)

        r_l_root = Node("m1", display_name="m", parent=r_root)
        r_r_root = Node("m2", display_name="m", parent=r_root)
        r_l_c = Node(numexp[0], parent=r_l_root)
        r_r_c = Node(numexp[1], parent=r_r_root)

    elif op == "MTA" or op == "MTS":
        if not numeral_only:
            l_root = Node(form[2], parent=root)
            l_l_0 = Node(form[0], parent=l_root)
            l_l_1 = Node(form[1], parent=l_l_0)
            l_r = Node(form[3], parent=l_root)
        if op == "MTA":
            r_root = Node("+", parent=root)
        else:
            r_root = Node("-", parent=root)
        if not numeral_only:
            r_l_r = Node(u'\u2715'.encode("utf-8"), parent=r_root)
            r_l_l = Node("m1", display_name="m", parent=r_l_r)
            r_l_l_1 = Node(numexp[0], parent=r_l_l)
            r_l_r = Node("m2", display_name="m", parent=r_l_r)
            r_l_r_1 = Node(numexp[1], parent=r_l_r)
            r_r = Node("m3", display_name="m", parent=r_root)
            r_r_1 = Node(numexp[2], parent=r_r)

    elif op == "MTA_LONG":
        levels = len(form) - 2
        base_tree = make_tree(form, numexp, "ADD", numeral_only)
        base_l = base_tree.children[0]
        base_r = base_tree.children[1]

        base_l.parent = None
        base_r.parent = None

        prev_level_l = base_l
        prev_level_r = base_r
        for i in range(levels):
            r_level = Node("+")
            r_l = Node("*", parent=r_level)
            r_1 = Node("m" + str(i) + "0", display_name="m", parent=r_l)
            mult = Node(numexp[len(form) - 2 - i], parent=r_1)
            r_2 = Node("m" + str(i) + "1", display_name="m", parent=r_l)
            base = Node("B ^ " + str(len(form) - i), parent=r_2)

            l_level = Node("-")
            l_l = Node(form[len(form) - 2 - i], parent=l_level)

            r_level.children = [r_l, prev_level_r]
            l_level.children = [l_l, prev_level_l]

            prev_level_l = l_level
            prev_level_r = r_level
        
        root.children = [prev_level_l, prev_level_r]


    return root


def build_language(langcode, stored_info=None, save=True, prnt=False):
    if stored_info:
        with open(stored_info, "rb") as f:
            lang_info = pickle.load(f)
            if langcode in lang_info:
                return lang_info[langcode]
    langcodes = [i[0] for i in inspect.getmembers(
        langstrategy, inspect.isfunction) if len(i[0]) == 3]

    if langcode not in langcodes:
        print("Please enter a valid language code (see complexities/langcodes.txt)")
        return

    strat_res, num_type, ulim = eval("langstrategy." + langcode)()
    complexity = calc_complexity(strat_res)

    if prnt:
        forest_disp(strat_res, langcode)

    if save:
        lang_info = {}
        if stored_info:
            with open(stored_info, "rb") as f:
                lang_info = pickle.load(f)

        lang_info[langcode] = (complexity, num_type, ulim)
    return complexity, num_type, ulim


def calc_complexity_base(tree):
    """Calculates the complexity (defined by number of nodes)"""
    return len([node for node in LevelOrderIter(tree)])


def calc_complexity(forest):
    total = 0
    for tree in forest:
        total += calc_complexity_base(tree)
    return total


def disp(tree, filename=None):
    #if filename != None:
        #RenderTreeGraph(tree).to_picture(os.path.abspath(filename + ".png"))
    return RenderTree(tree)


def forest_disp(forest, langcode):
    if not os.path.exists(langcode):
        os.makedirs(langcode)
    for i, tree in enumerate(forest, 1):
        disp(tree, langcode + "/" + str(i))
    return


def print_grammar(forest, num_type, langcode):
    num_types = {"0": "restricted approximate", "1": "restricted exact", "2": "body part",
                 "3": "other base", "4": "vigesimal", "5": "hybrid", "6": "decimal"}
    langcodes = {"acg": "Achagua", "ain": "Ainu", "ana": "Araona", "awp": "Awa Pit", "brs": "Barasuno", "bae": "Bar" + u'\u00E9', "eng": "English", "geo": "Georgian", "goo": "Gooniyandi", "hix": "Hixkaryana", "hpd": "Hup", "imo": "Imonda", "kay": "Kayardild",
                 "mnd": "Mandarin", "myi": "Mangarrayi", "mrt": "Martuthunira", "pit": "Pitjantjatjara", "prh": "Pirah" u'\u00E3', "ram": "Rama", "war": "Wari", "wsk": "Waskia", "wch": "Wichu'00ED'", "yid": "Yidiny", "xoo": u'\u0021' + "X" + u'\u00F3' + u'\u00F5',
                 "fre": "French", "spa": "Spanish"}

    print(langcodes[langcode] + ": \t {")
    print("type: " + num_types[str(num_type)])
    print("}")
    forest_disp(forest, langcode)
    return


if __name__ == "__main__":
    #t = make_tree(["fsdf", "dsfsd", "-", "dsifhsd", "sfdf"], ["fsdf-dsfsd", "dsifhsd-sfdf"], "ADD")
    #print(disp(t, "trial_multi"))
    #print(build_language("acg", prnt=True))

    """f = open("complexities/selected.txt", "r")
    selected_25 = f.read().split('\r\n')
    for l in selected_25:
        print(l + ":")
        print(build_language(l, True))"""
    forest = build_language("ain", prnt=True)
    print(forest)
    assert False

    print(print_grammar(forest, 6, "mnd"))

    root = Node("=")

    l_root = Node("-", parent=root)
    l_0 = Node("u", parent=l_root)
    l_1 = Node("v", parent=l_root)
    l_0_0 = Node("ty", parent=l_0)

    r_root = Node("+", parent=root)
    r_0 = Node("*", parent=r_root)
    r_1 = Node("m0", parent=r_root)
    r_0_0 = Node("m1", parent=r_0)
    r_0_1 = Node("m2", parent=r_0)
    r_0_0_0 = Node("u1", parent=r_0_0)
    r_0_1_0 = Node("ten", parent=r_0_1)
    r_1_0 = Node("v1", parent=r_1)

    DotExporter(root).to_dotfile("mta.dot")