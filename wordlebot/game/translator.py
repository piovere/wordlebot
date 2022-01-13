from typing import Dict
import string
import numpy as np

def chardict() -> Dict[str, int]:
	"""A dictionary mapping characters to their indices
	
	Examples
	--------
	>>> chardict()
	{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, \
'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, \
'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, \
'z': 26}
	"""
	letters = list(string.ascii_lowercase)
	ret = {l: i+1 for i, l in enumerate(letters)}
	return ret

def word_to_vec(word: str):
	"""Convert word to 1-hot vector"""
	assert len(word) == 5

	word = word.lower()

	cd = chardict()

	ret = np.zeros((5, 27), dtype=bool)

	for i, letter in enumerate(list(word)):
		out[i, dc[letter]] = True

	return ret

def vec_to_word(vec: np.ndarray):
	"""Convert from a 2D numpy array to a string"""
	v = np.argmax(vec, axis=1)
	dc = {v: k for k, v in chardict().items()}
	chars = [dc[vi] for vi in v]
	return "".join(chars)
