
def plot_err_over_time(filename):
	dictionary = {"english": {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "twenty": 20}, 
		      "chinese": {"yi": 1, "er": 2, "san": 3, "shi": 4, "wu": 5, "liu": 6, "qi": 7, "ba": 8, "jiu": 9, "shi": 10, "ershi": 20}}
	f = open(filename, "w")
	
	eng_points = []
	eng_mod_points = []
	chn_points = []
	chn_mod_points = []
	for line in f.readlines():
		split_line = line.split(',')
		number = int(split_line[0])
		eng_words = split_line[1].split('-')
		eng_mod = split_line[2].split('-')
		chn_words = split_line[3].split('-')
		chn_mod = split_line[4].split('-')	
		
		seq_eng_0 = []
		seq_eng_1 = []
		seq_chn_0 = []
		seq_chn_1 = []
		for i in range(len(eng_words)):
			if i == 0:
				seq_eng_0.append(dictionary["english"][eng_words[i]])
			else:
				seq_eng_0.append(dictionary["english"][eng_words[i]] + seq_eng_0[i - 1])

		for i in range(len(eng_mod)):
			if i == 0:
				seq_eng_1.append(dictionary["english"][eng_mod[i]])
			else:
				seq_eng_1.append(dictionary["english"][eng_mod[i]] + seq_eng_1[i - 1])
		
		eng_points.extend([(number, abs(number - seq_eng_0[i]) for i in len(seq_eng_0))])
		eng_mod_points.extend([number, abs(number - seq_eng_1[i]) for i in len(seq_eng_1)])
		

if __name__ == "__main__":
	f = open("atom_base.csv", "w")
		
