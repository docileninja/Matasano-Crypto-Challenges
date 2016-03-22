#! /usr/bin/python
# Challenge 4 - Detect single-character XOR

import binascii
from pprint import pprint
from utils import single_xor, rate_string, recover_single_key

with open('4.txt', 'r') as f:
	ciphertexts = []
	for ciphertext in f:
		ciphertexts.append(binascii.a2b_hex(ciphertext.strip()))

possible_decryptions = []
for ciphertext in ciphertexts:
	key = recover_single_key(ciphertext)
	possible_plaintext = single_xor(ciphertext, key)
	possible_decryptions.append((key, possible_plaintext))

print("sorting")
pprint(sorted(possible_decryptions, key=lambda tp: rate_string(tp[1]))[-1])