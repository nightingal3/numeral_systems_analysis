import inspect
import math
import matplotlib
matplotlib.use("Agg")
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

    colors_per_term = { 
        1: ["#e50012"],
        3: ["#e50012", "#750068", "#0500bf"],
        4: ["#e50012", "#9a004b", "#4f0085", "#0500bf"],
        5: ["#e50012", "#ad003d", "#750068", "#3d0093", "#0500bf"],
        6: ["#e50012", "#b80034", "#8b0057", "#5e0079", "#31009c", "#0500bf"],
        10: ["#e50012", "#d00021", "#bc0031", "#a70041", "#930050", "#7f0060", "#6a0070", "#560080", "#42008f", "#2d009f", "#1900af", "#0500bf"],
        14: ["#e50012", "#d6001d", "#c70029", "#b80034", "#a90040", "#9a004b", "#8b0057", "#7c0062", "#6d006e", "#5e0079", "#4f0085", "#400090", "#31009c", "#2200a7", "#1300b3", "#0500bf"],
        15: ["#e50012", "#d5001e", "#c5002a", "#b50037", "#a50043", "#a50037", "#95004f", "#85005c", "#750068", "#650074", "#550081", "#45008d", "#350099", "#2500a6", "#1500b2", "#0500bf"]
    }

    offsets = {"Piraha": -0.4, "Gooniyandi": -0.7, "Achagua": -0.55, "Kayardild": -0.6, "Wichi": -0.35, "English": -0.45}

    bound_approx_systems = len(lang_term_bounds["Approximate"]) * 3
    bound_exact_systems = len(lang_term_bounds["Exact"]) * 3 
    bound_recursive_systems = len(lang_term_bounds["Recursive"]) * 3 

    colorbar_gen = create_colorbar_generator(axes, colors_per_term, offsets, num_rows, num_cols)
    offset = colorbar_gen(bound_approx_systems, lang_term_bounds["Approximate"], "Approximate", ideal_bounds_approx_flat)
    offset = colorbar_gen(bound_exact_systems + offset, lang_term_bounds["Exact"], "Exact", ideal_bounds_exact_flat)
    colorbar_gen(bound_recursive_systems + offset, lang_term_bounds["Recursive"], "Recursive", {14:[i for i in range(1, 16)]})
    plt.subplots_adjust(left=0.13,bottom=0.21,right=0.94,top=0.89,wspace=0.76,hspace=0.65)
    plt.savefig("colormaps_flat.png")
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

def plot_colorbar(ax, colors, bounds, text, x_offset = -0.7, y_offset = 0.3):
    norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=1)
    if len(bounds) != 2:
        norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=len(bounds) - 2)
    
    ax.tick_params(axis='both', which='minor', labelsize=5)

    cmap = matplotlib.colors.ListedColormap(colors)
    colorbar = matplotlib.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation="horizontal", spacing="proportional")

    colorbar.set_ticks([i for i in range(0, 16, 5)])

    if text != "Optimal":
        ax.axis("on")
        colorbar.set_ticklabels([i for i in range(0, 16, 5)])

    ax.text(x_offset, y_offset, text, fontsize=10)


def round_up_to_nearest(num_to_round, base):
    return int(math.ceil(float(num_to_round) / base) * base)

if __name__ == "__main__":
    plot_terms_gradient(lang_term_bounds)
