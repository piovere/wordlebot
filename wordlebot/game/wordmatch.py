import numpy as np

def yellows(guess: str, target: str):
	"""Find the yellow letters in the guess
	
	Examples
	--------
	>>> g = 'abcde'
	>>> t = 'edcba'
	>>> yellows(g, t)
	[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
	>>> g = 'efghi'
	>>> yellows(g, t)
	[('e', 0)]
	"""
	out = []
	for i, g in enumerate(guess):
		if g in target:
			out.append((g, i))
			target = target.replace(g, '', 1)
	return out

def greens(guess: str, target: str):
	"""Find the green letters in the guess
	
	Examples
	--------
	>>> g = 'abcde'
	>>> t = 'fgcdh'
	>>> greens(g, t)
	[('c', 2), ('d', 3)]
	"""
	greens = [(g, i) for i, (g, t) in enumerate(zip(guess, target)) if g == t]
	return greens
	
def grade(guess: str, target: str) -> np.ndarray:
	"""Evaluate a guess against the true word"""
	out = np.zeros((5, 26+26+26+1), dtype=bool)
	
	gs = greens(guess, target)
	ys = yellows(guess, target)
	
	raise NotImplementedError("Still need to do the combined output")
	
	return out
