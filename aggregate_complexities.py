import os

def aggregate_complexities(langlist):
	langs = []
	with open(langlist, "r") as f:
		langs = f.split('\r\n')
	
	complexities = dict((i, 0) for i in range(7))
	
	for lang in langs:
		curr_complexity, lang_type = build_language(lang)
		complexities[lang_type] += curr_complexity

	return complexities
		
