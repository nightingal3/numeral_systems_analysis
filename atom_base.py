import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy
import numpy as np
import matplotlib.ticker as ticker

def err_over_time(filename):
	eng_dictionary = {"one": 1, "two": 2, "three": 3, "thir": 3, "four": 4, "five": 5, "fif": 5, "six": 6, "seven": 7, "eight": 8, "eigh": 8, "nine": 9, "teen": 10, "eleven": 11, "twelve": 12, "twenty": 20, "thirty": 30}
	chn_dictionary =  {"yi": 1, "er": 2, "san": 3, "si": 4, "wu": 5, "liu": 6, "qi": 7, "ba": 8, "jiu": 9, "shi": 10, "ershi": 20}
	reverse_dictionary_eng = {value: key for key, value in eng_dictionary.items()}
	reverse_dictionary_chn = {value: key for key, value in chn_dictionary.items()}
	f = open(filename, "r")
	eng_points = []
	eng_mod_points = []
	chn_points = []
	chn_mod_points = []


	number = []
	eng_words = []
	eng_mod = []
	chn_words = []
	chn_mod = []
	for line in f.readlines():
		split_line = line.split(',')
		number.append(int(split_line[0]))
		eng_words.append(split_line[1].split('-'))
		eng_mod.append(split_line[2].split('-'))
		#chn_words.append(split_line[3].split('-'))
		#chn_mod.append(split_line[4].split('-'))	
		
	seq_eng_0 = []
	seq_eng_1 = []
	seq_chn_0 = []
	seq_chn_1 = []
	for i in range(len(number)):
		temp = []
		for j in range(len(eng_words[i])):
			if j == 0:
				temp.append((len(eng_words[i][j]), number[i], eng_dictionary[eng_words[i][j]], j))
			else:
				temp.append((len(eng_words[i][j]), number[i], eng_dictionary[eng_words[i][j]] + eng_dictionary[eng_words[i][j - 1]], j))
		seq_eng_0.extend(temp)
                temp1 = []
		for j in range(len(eng_mod[i])):
			if j == 0:
				temp1.append((len(eng_mod[i][j]), number[i], eng_dictionary[eng_mod[i][j]], j))
			else:
				temp1.append((len(eng_mod[i][j]), number[i], eng_dictionary[eng_mod[i][j]] + eng_dictionary[eng_mod[i][j - 1]], j))
		seq_eng_1.extend(temp1)


	#print(seq_eng_1)
	res0 = []
	res1 = []
	for i in range(len(seq_eng_0)):
		if seq_eng_0[i][3] == 0:
			res0.append((seq_eng_0[i][0], find_err(seq_eng_0[i][1], seq_eng_0[i][2]), seq_eng_0[i][1]))
		else:
			res0.append((seq_eng_0[i][0] + seq_eng_0[i - 1][0], find_err(seq_eng_0[i][1], seq_eng_0[i][2]), seq_eng_0[i][1]))

	for i in range(len(seq_eng_1)):
		if seq_eng_1[i][3] == 0:
			res1.append((seq_eng_1[i][0], find_err(seq_eng_1[i][1], seq_eng_1[i][2]), seq_eng_1[i][1]))
		else:
			res1.append((seq_eng_1[i][0] + seq_eng_1[i - 1][0], find_err(seq_eng_1[i][1], seq_eng_1[i][2]), seq_eng_1[i][1]))

	#print(res1)
	
		#eng_points.extend([(number, abs(number - seq_eng_0[i]) for i in len(seq_eng_0))])
		#eng_mod_points.extend([number, abs(number - seq_eng_1[i]) for i in len(seq_eng_1)])
		
	return number, res0, res1

def plot_err_comparison(number_list, opt1, opt2):
	for number in number_list:
		series1 = [item[0:2] for item in opt1 if item[2] == number]
		series1.insert(0, (0, number))
		x0 = [i[0] for i in series1]
		y0 = [i[1] for i in series1]
		print("s1")
		print(x0)
		print(y0)
		#fit1 = scipy.optimize(curve_fit(lambda t, a, b: a + b * numpy.log(t), [i[0] for i in series1], [i[1] for i in series2]))
		series2 = [item[0:2] for item in opt2 if item[2] == number]
		series2.insert(0, (0, number))
		x1 = [j[0] for j in series2]
		y1 = [j[1] for j in series2]
		print("s2")
		print(x1)
		print(y1)
		plt.vlines(0, ymin=y0[0], ymax=number, lw=2, color="blue")
		plt.step(x0, y0, where="post", label="English attested")
		plt.vlines(x0[-1], ymin=0, ymax=y0[-1], lw=2, color="blue")
		diff = find_diff(series1, series2)
		if diff < 0:
			diff_col = "blue"
		elif diff > 0:
			diff_col = "orange"
		else:
			diff_col = "black"
		plt.text(10.5, 0, str(abs(diff)), color=diff_col)
		plt.step(x1, y1, where="post", label="English alternative")
		plt.xlabel("Characters read")
		plt.ylabel("Error")
		plt.xlim(xmin=0)
		plt.xticks(range(0, 12, 1)) 
		plt.yticks(range(0, number, 2))
		plt.title(number)
		plt.legend()
		filename = str(number) + ".png"
		plt.savefig(filename)
		plt.gcf().clear()


def find_diff(opt1, opt2, absolute=True):
	#returns area(opt1) - area(opt2) for step functions
	opt1_width = []
	opt1_height = []
	for i in range(1, len(opt1)):
		opt1_width.append(opt1[i][0] - opt1[i - 1][0])
		opt1_height.append(opt1[i - 1][1])
	opt1_area = sum([opt1_width[i] * opt1_height[i] for i in range(len(opt1_width))])
	print("opt1 area")
	print(opt1_width)
	print(opt1_height)
	print(opt1_area)
	opt2_width = []
	opt2_height = []
	for i in range(1, len(opt2)):
		opt2_width.append(opt2[i][0] - opt2[i - 1][0])
		opt2_height.append(opt2[i - 1][1])

	opt2_area = sum([opt2_width[i] * opt2_height[i] for i in range(len(opt2_width))])
	print("opt2 area")
	print(opt2_width)
	print(opt2_height)
	print(opt2_area)
	return opt1_area - opt2_area

def plot_diff_seq(numbers, opt1, opt2):
	diffs = []
	for number in numbers:
                series1 = [item[0:2] for item in opt1 if item[2] == number]
		series1.insert(0, (0, number))
		x0 = [i[0] for i in series1]
		y0 = [i[1] for i in series1]

		series2 = [item[0:2] for item in opt2 if item[2] == number]
		series2.insert(0, (0, number))
		x1 = [j[0] for j in series2]
		y1 = [j[1] for j in series2]
		
		diffs.append(find_diff(series1, series2))
        print(diffs)
	plt.bar(numbers, diffs)
	plt.title("Numeral vs. Relative advantage of base-atom form")
	plt.xlabel("Numeral")
	plt.ylabel("error over time of base-atom - error over time of atom-base")
	plt.savefig("base_atom_advantage.png")
	plt.gcf().clear()		

def find_err(target_num, guess):
	return abs(target_num - guess)	

if __name__ == "__main__":
	#print(find_diff([(0, 21), (6, 1), (9, 0)], [(0, 21), (3, 20), (9, 0)]))
	x = err_over_time("atom_base_2.csv")
       	print(x)
	plot_diff_seq(x[0], x[1], x[2])
        #diff = plot_err_comparison(x[0], x[1], x[2])

		
