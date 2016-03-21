import binascii
from pprint import pprint
from utils import letter_frequencies, single_xor, rate_string

with open('4.txt', 'r') as f:
	ciphertexts = []
	for ciphertext in f:
		ciphertexts.append(binascii.a2b_hex(ciphertext.strip()))

possible_decryptions = []
for i in range(256):
	for ciphertext in ciphertexts:
		possible_decryption = single_xor(ciphertext, i)
		possible_decryptions.append(possible_decryption)

print("sorting")
pprint(sorted(possible_decryptions, key=rate_string)[-1])