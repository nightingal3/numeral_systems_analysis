import numpy as np
from inspect import isfunction

def find(iterable, cond, axis=0):
	if isinstance(iterable, list) and callable(cond):
		return [i for i, val in enumerate(iterable) if cond(val)]
	elif isinstance(iterable, list) and not callable(cond):
		return [i for i, val in enumerate(iterable) if val == cond]
	elif isinstance(iterable, np.ndarray):
		if iterable.ndim == 1:
			return find(list(iterable), cond)
		else:
			if callable(cond):
				return [index for index, elem in np.ndenumerate(iterable) if cond(elem)]
		 	else:
				if isinstance(cond, np.ndarray):
					if cond.ndim == 1:
						res = []
						for i in range(iterable.shape[axis]):
							for j in range(iterable.shape[abs(axis - 1)]): #only supports 2d arrays for now
								if axis == 0:
									if iterable[i, j] == cond[i]:
										res.append(j)
										print(j)
								else:
									if iterable[j, i] == cond[i]:
										res.append(j) 
						return res
					
					elif cond.ndim == 0:
						return 	[index for index, elem in np.ndenumerate(iterable) if elem == cond]
					else:
						raise NotImplementedError
def find_diff(X, Y):	
	#to match matlab implementation
	return sorted(set(X) - set(Y))

def find_unique(X):
	return sorted(set(X))


if __name__ == "__main__":
	print(find([1, 2, 3, 6, 999], 999))
	print(find([1, 2, 3, 6, 999], lambda x: x > 5))
	print(find(np.zeros(3, ), lambda x: x == 0))
	print(find(np.zeros((1, 2)), lambda x: x == 0))
