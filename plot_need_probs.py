import itertools
import sys
import os
import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


def plot_need_probs_from_csvs(dirpath, plot_all=True):
    """Generates multiple lines in the form {line: [pt1, pt2....]}.
    Assumes that source files are single column csv files containing pts. """
    probs = {}

    if not os.path.isdir(dirpath):
        print("Directory does not exist.")
        sys.exit(1)
    for filename in os.listdir(dirpath):
        if filename.endswith(".csv"):
            try:
                with open(os.path.join(dirpath, filename), "r") as csv_file:
                    reader = csv.reader(csv_file)
                    for row in enumerate(reader):
                        # print(row)
                        if filename not in probs:
                            probs[filename] = [float(row[1][0])]
                        else:
                            probs[filename].append(float(row[1][0]))
            except IOError as e:
                print(e)
                print("Could not open file " + filename)
                if plot_all:
                    print("Exiting...")
                    sys.exit(1)
                continue
    print(probs)
    return probs


def plot_multiple_lines(lines_dict, main_line=None, save_file="multi_line_plot.eps", shift=0):
    """Lines dict should be organized {line1: [pt1, pt2...]}
       The main line is the one that should be emphasized."""
    colors = ["blue", "lightcoral", "goldenrod", "violet",
              "mediumseagreen", "dodgerblue", "orange", "chocolate"]
    color_generator = itertools.cycle(colors)
    for line in sorted(lines_dict.keys()):
        print(line)
        print(len(lines_dict[line]))
        linename = line
        if line.endswith(".csv"):
            linename = line[:-4]
        numberline = [i+shift for i in range(len(lines_dict[line]))]
        print(numberline)
        if line == main_line:
            plt.plot(numberline, lines_dict[line], color="black",
                     label=linename, lw=3, zorder=float("inf"))
        else:
            plt.plot(numberline, lines_dict[line], color=next(
                color_generator), label=linename, alpha=0.6)
    plt.legend(prop={"size": 16})
    plt.xticks([i for i in range(0, 100, 10)], fontsize=16)
    plt.yticks([0.01 * j for j in range(0, 20, 5)], fontsize=16)
    plt.xlabel("Number Line", fontsize=20)
    plt.ylabel("Normalized frequency", fontsize=20)
    plt.tight_layout()
    #plt.title("Normalized frequencies of numerals across languages")
    plt.savefig(save_file)
    plt.gcf().clear()


if __name__ == "__main__":
    probs = plot_need_probs_from_csvs(
        "./data/need_probs/sample", plot_all=False)
    plot_multiple_lines(probs, main_line="Average.csv", shift=1)
