import inspect
import math
import matplotlib
#matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt

from routines.get_term_num_matrix import get_term_num_matrix
import langstrategy
import language_tree


lang_term_bounds = {
    "Approximate": [("Piraha", [0, 1, 2, 5, 15]), ("Gooniyandi", [0, 1, 2, 3, 5, 7, 15])],
    "Exact": [("Achagua", [0, 1, 2, 3, 15]), ("Kayardild", [0, 1, 2, 3, 4, 5, 15]), ("Yidiny", [0, 1, 2, 3, 4, 5, 15]), ("Wichi", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])],
    "Recursive": [("English", [i for i in range(0, 16)])]
}


ideal_bounds_approx_steep = {
    3: [0, 1, 2, 6, 15],
    5: [0, 1, 2, 3, 4, 11, 15],
    6: [0, 1, 2, 3, 4, 6, 12, 15]
}

ideal_bounds_approx = {
    3: [0, 1, 2, 6, 15],
    5: [0, 1, 2, 3, 5, 11, 15],
    6: [0, 1, 2, 3, 4, 6, 12, 15]
}

ideal_bounds_approx_flat = {
    3: [0, 11, 15],
    5: [0, 1, 5, 11, 15],
    6: [0, 1, 4, 8, 12, 15]
}

bad_bounds_approx = {
    3: [0, 10, 21, 56, 100], # comp: 11, cost: 3.88  mus: [20, 21, 92]
    4: [0, 1, 36, 52, 73, 100], # comp: 16, cost: 3.65   mus: [65, 82, 33, 38]
    5: [0, 1, 6, 21, 54, 100], # comp: 20, cost: 3.72  mus: [1, 11, 32, 77, 89]
    6: [0, 4, 5, 6, 12, 43, 66, 100] # comp: 24, cost: 3.61 mus: [1, 6, 22, 39, 54, 61]
}

worst_bounds_exact = {
    #3: [0, 98, 99, 100], # comp: 10, cost: 15.45
    5: [0, 96, 97, 98, 99, 100], # comp: 17, cost: 8.21
    6: [0, 95, 96, 97, 98, 99, 100], # comp: 21, cost: 6.56
    7: [0, 94, 95, 96, 97, 98, 99, 100], # comp: 25, cost: 5.88
    8: [0, 93, 94, 95, 96, 97, 98, 99, 100] # comp: 29  cost: 5.51

}

colors_per_term = { 
        1: ["#3182bd"],
        3: ["#3182bd", "#6baed6", "#9ecae1"],
        4: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef"],
        5: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c"],
        6: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b"],
        7: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2"],
        8: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354"],
        9: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354", "#74c476"],
        10: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#756bb1"],
        14: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#756bb1", "#9e9ac8", "#bcbddc", "#dadaeb", "#636363"],
        15: ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#756bb1", "#9e9ac8", "#bcbddc", "#dadaeb", "#636363"]
}

def gen_ideal_bounds_exact(n): return [i for i in range(0, n + 1)] + [15]
def gen_ideal_bounds_exact_flat(n): return [i for i in range(0, 15, int(round(100 / n)))] + [15]
ideal_bounds_exact = {i: gen_ideal_bounds_exact(i) for i in range(3, 16)}
ideal_bounds_exact_flat = {i: gen_ideal_bounds_exact_flat(i) for i in range(3, 16)}

ideal_bounds_exact_steep = ideal_bounds_exact

def get_langterms():
    # assume naming convention is respected...
    langlist = [i[0] for i in inspect.getmembers(
        langstrategy, inspect.isfunction) if len(i[0]) == 3]
    term = {"prh": ["hoi_1", "hoi_2", "aibaagi"], "war": ["xica pe", "dois"], "goo": ["yoowarni", "garndiwiddidi", "ngarloodoo", "marla"],
            "acg": ["bague", "chamai", "matalii"], "kay": ["warngiida", "kiyarrngka", "burldamurra", "mirdinda", "muthaa"], "yid": ["guman", "jambul", "dagul", "yunggan gunyjii", "mala"], "wch": ["wenyala", "tagw", "najtefwayal", "fwantes ihi", "qwe wenyal", "ipofwuj", "ipofwustoj", "ipofwusfwaya el", "ipofwusfwantes ihi", "oqwecho taqs"],
            "eng": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]}
    num_term_pt = {"prh": [1, 2, 2, 2, 3, 3, 3, 3, 3, 3], "war": [1, 2], "goo": [1, 2, 3, 3, 4],
                    "acg": [1, 2, 3], "kay": [1, 2, 3, 4, 5], "yid": [1, 2, 3, 4, 5], "wch": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    end_category = {"prh": 0, "war": 0, "goo": 0,
                    "acg": 1, "kay": 1, "yid": 1, "wch": 1,
                    "eng": 6}

    for langcode in term:
        _, num_type, ulim = eval("langstrategy." + langcode)()

        get_term_num_matrix(term[langcode], len(
            term[langcode]), num_term_pt[langcode], num_type, [i for i in range(1, 101)])


def plot_terms_gradient(term_maps):
    num_rows, num_cols = 15, 3
    fig, axes = plt.subplots(num_rows, num_cols)
    axes = axes.T.ravel()
    for ax in axes:
        ax.axis("off")

    new_cmap = matplotlib.cm.get_cmap("tab20c")
    for i in range(new_cmap.N):
        rgb = new_cmap(i)[:3]
        print(matplotlib.colors.rgb2hex(rgb))
    #assert False
    offsets = {"Piraha": -0.4, "Gooniyandi": -0.7, "Achagua": -0.55, "Kayardild": -0.6, "Wichi": -0.35, "English": -0.45}

    bound_approx_systems = len(lang_term_bounds["Approximate"]) * 3
    bound_exact_systems = len(lang_term_bounds["Exact"]) * 3 
    bound_recursive_systems = len(lang_term_bounds["Recursive"]) * 3 

    colorbar_gen = create_colorbar_generator(axes, colors_per_term, offsets, num_rows, num_cols)
    offset = colorbar_gen(bound_approx_systems, lang_term_bounds["Approximate"], "Approximate", ideal_bounds_approx)
    offset = colorbar_gen(bound_exact_systems + offset, lang_term_bounds["Exact"], "Exact", ideal_bounds_exact)
    colorbar_gen(bound_recursive_systems + offset, lang_term_bounds["Recursive"], "Recursive", {14:[i for i in range(1, 16)]})
    plt.subplots_adjust(left=0.13,bottom=0.21,right=0.94,top=0.89,wspace=0.76,hspace=0.65)
    plt.savefig("colormaps_new.png")
    plt.gcf().clear()

def plot_inefficient_systems():
    num_rows, num_cols = 10, 2
    fig, axes = plt.subplots(num_rows, num_cols)
    axes = axes.T.ravel()
    for ax in axes:
        ax.axis("off")
    new_cmap = matplotlib.cm.get_cmap("tab20c")
    for i in range(new_cmap.N):
        rgb = new_cmap(i)[:3]
        print(matplotlib.colors.rgb2hex(rgb))

    offsets = {}
    samples0 = ["A1", "A2", "A3", "A4"]
    offsets0 = [0.5] * 4
    samples1 = ["E1", "E2", "E3", "E4"]
    offsets1 = [0.5] * 4

    colorbar_gen = create_spaced_single_colorbar_gen(axes, colors_per_term, offsets, num_rows, num_cols)
    offset = colorbar_gen(len(bad_bounds_approx) * 2, bad_bounds_approx, samples0)
    colorbar_gen(offset + len(worst_bounds_exact) * 2, worst_bounds_exact, samples1)

    #plt.show()
    plt.subplots_adjust(left=0.18,bottom=0.21,right=0.88,top=0.89,wspace=0.70,hspace=0.65)
    #plt.tight_layout()
    plt.savefig("worst_bounds.png")
    plt.gcf().clear()

    

ax_ind = 0
def create_colorbar_generator(axes, colors, text_offset, num_rows, num_cols):
    def next_group(upper_bound, langs, type, ideal_bounds):
        global ax_ind
        if ax_ind > num_rows * num_cols:
            raise StopIteration("Attempting to iterate outside created axes")
       
        for i, (ideal_ax, attested_ax, empty_ax) in enumerate(zip(axes[ax_ind + 1:upper_bound:3], axes[ax_ind + 2:upper_bound:3], axes[ax_ind:upper_bound:3])):
            del empty_ax
            name, attested_bounds = lang_term_bounds[type][i]
            num_terms = len(attested_bounds) - 2
            color_list = colors[num_terms]
            attested_offset = text_offset[name] if name in text_offset else -0.4
            
            plot_colorbar(attested_ax, color_list, attested_bounds, name, attested_offset)
            plot_colorbar(ideal_ax, color_list, ideal_bounds[num_terms], "Optimal", x_offset = -0.5)
        ax_ind = round_up_to_nearest(upper_bound, num_rows) # Fill in whitespace
        return ax_ind
    
    return next_group

ax_ind_single = 0
num_called = 0

def create_spaced_single_colorbar_gen(axes, colors, text_offset, num_rows, num_cols):
    def next_group(upper_bound, term_bounds, text):
        global ax_ind_single
        global num_called
        for i, (term_ax, empty_ax) in enumerate(zip(axes[ax_ind_single:upper_bound:2], axes[ax_ind_single + 1:upper_bound:2])):
            del empty_ax
            print(num_called)
            num_terms = list(term_bounds.keys())[num_called]
            num_called += 1
            bad_bounds = term_bounds[num_terms]
            color_list = colors[num_terms]
            offset = -0.2
            ticks = [1, 10, 25, 50, 100]

            plot_colorbar(term_ax, color_list, bad_bounds, text[i], x_offset=offset, ticks=ticks)
        
        ax_ind_single = round_up_to_nearest(upper_bound, num_rows)
        num_called = 0
        return ax_ind_single
    
    return next_group

def plot_colorbar(ax, colors, bounds, text, x_offset = -0.7, y_offset = 0.3, ticks=[1, 2, 3, 4] + [i for i in range(5, 16, 5)]):
    norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=1)
    if len(bounds) != 2:
        norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=len(bounds) - 2)
    
    ax.tick_params(axis='both', which='minor', labelsize=5)

    cmap = matplotlib.colors.ListedColormap(colors)
    colorbar = matplotlib.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation="horizontal", spacing="proportional")

    colorbar.set_ticks(ticks)

    if text != "Optimal":
        ax.axis("on")
        colorbar.set_ticklabels(ticks)

    ax.text(x_offset, y_offset, text, fontsize=9)


def round_up_to_nearest(num_to_round, base):
    return int(math.ceil(float(num_to_round) / base) * base)

if __name__ == "__main__":
    plot_terms_gradient(lang_term_bounds)
    #plot_inefficient_systems()