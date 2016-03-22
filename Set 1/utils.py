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

def fixed_xor(b1, b2):
	return bytes(c1 ^ c2 for c1, c2 in zip(b1, b2))

def single_xor(s, k):
	return bytes(c ^ k for c in s)

from itertools import cycle
def repeating_xor(s, k):
	return fixed_xor(s, cycle(k))


from math import log
def rate_string(s):
	prob = 0
	for c in s:
		char = chr(c).lower()
		prob += log(letter_frequencies.get(char, .0000001))
	return prob

def hamming_distance(b1, b2):
	def num_one_bits(n):
		if n == 0:
			return 0
		else:
			return 1 + num_one_bits(n & (n - 1))
		
	return sum(num_one_bits(c1 ^ c2) for c1, c2 in zip(b1, b2))

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def recover_single_key(ciphertext):
	possible_decryptions = []
	for i in range(256):
		possible_decryption = single_xor(ciphertext, i)
		possible_decryptions.append((i, possible_decryption))
	ranked_decryptions = sorted(possible_decryptions, key=lambda tp: -rate_string(tp[1]))
	return ranked_decryptions[0][0]