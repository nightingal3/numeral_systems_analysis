

def find(lst, cond):
	if callable(cond):
		return [i for i, val in enumerate(lst) if cond(val)]
	else:
		return [i for i, val in enumerate(lst) if val == cond]


