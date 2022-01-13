from typing import Dict
import string
import numpy as np

def chardict() -> Dict[str, int]:
	letters = list(string.ascii_lowercase)
	ret = {}
	for i in range(1, 27):
		ret[letters[i-1]] = i
	return ret

def word_to_vec(word: str):
	"""Convert word to 1-hot vector"""
	wordlen = 5


