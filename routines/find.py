

def find(lst, cond):
	return [i for i, val in enumerate(lst) if cond(val)]

