from num2words import num2words
import csv
import sys

def write_words(upper_bound, filename):
	numfile = open(filename, "wb")
	writer = csv.writer(numfile)
	writer.writerow(["Number", "Reading"])
	for i in range(1, upper_bound):
		writer.writerow([i, num2words(i)])
	
	numfile.close()
	print("Done.")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: write_words.py filename upper_bound")
		sys.exit(1)
	if sys.argv[1][-4:] != ".csv":
		print("Filename must end with .csv")
		sys.exit(1)
	upper_bound = int(sys.argv[2])
	
	write_words(upper_bound, sys.argv[1]) 
