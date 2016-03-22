#! /usr/bin/python
# Challenge 3 - Single-byte XOR cipher

import binascii
from utils import letter_frequencies, single_xor

from math import log
def rate_string(s):
	prob = 0
	for c in s:
		char = chr(c).lower()
		prob += log(letter_frequencies.get(char, .0000001))
	return prob

def recover_single_key(ciphertext):
	possible_decryptions = []
	for i in range(256):
		possible_decryption = single_xor(ciphertext, i)
		possible_decryptions.append((i, possible_decryption))
	ranked_decryptions = sorted(possible_decryptions, key=lambda tp: -rate_string(tp[1]))
	return ranked_decryptions[0][0]

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte_string = binascii.a2b_hex(hex_string)

key = recover_single_key(byte_string)
print(key)
plaintext = single_xor(byte_string, key)
print(plaintext)