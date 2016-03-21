letter_frequencies = {
	'a': .082,
	'b': .015,
	'c': .028,
	'd': .043,
	'e': .127,
	'f': .022,
	'g': .020,
	'h': .061,
	'i': .070,
	'j': .002,
	'k': .008,
	'l': .040,
	'm': .024,
	'n': .067,
	'o': .075,
	'p': .019,
	'q': .001,
	'r': .060,
	's': .063,
	't': .091,
	'u': .028,
	'v': .010,
	'w': .024,
	'x': .002,
	'y': .020,
	'z': .001,
	' ': .001
}

def single_xor(s, k):
	return bytes(c ^ k for c in s)

from math import log
def rate_string(s):
	prob = 0
	for c in s:
		char = chr(c).lower()
		prob += log(letter_frequencies.get(char, .0000001))
	return prob