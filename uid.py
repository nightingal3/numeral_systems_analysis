

def read_file(filename):
	f = open(filename, "r");
	number = []
	eng_words = []
	eng_mod = []
	chn_words = []
	chn_mod = []

	for line in f.readlines():
		split_line = line.split(",")
		number.append(int(split_line[0])
		eng_words.append(split_line[1].split("-"))
		eng_mod.append(split_line[2].split("-"))

	f.close()
	return number, eng_words, eng_mod


def calc_entropy_trajectory(number, need_prob, **opts):
	eng_dict = {"one": 1, "two": 2, "three": 3, "thir": 3, "four": 4, "five": 5, "fif": 5, "six": 6, "seven": 7, "eight": 8, "eigh": 8, "nine": 9, "teen": 10, "twenty": 20}
	entropies = [val * math.log(1/float(val), 2) for key, val in need_prob] 
	base_H =  - sum(entropies)
	print(base_H)

	for name, opt in opts.iteritems():
		for i in range(number):
			pass


def calc_UID_deviation(H_traj, phrase_len):
	total = 0
	for i in range(phrase_len):
		if i == phrase_len - 1:
			I = H_traj[-1]
		else:
			I = H_traj[i] - H_traj[i + 1]
		total += abs(I/H_traj[0] - (1/3))

	return (3/4) * total
