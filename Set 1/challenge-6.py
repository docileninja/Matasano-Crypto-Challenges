#! /usr/bin/python
# Challenge 6 - Break repeating-key XOR

from utils import hamming_distance, chunks, recover_single_key, repeating_xor, rate_string
import binascii

with open('6.txt', 'r') as f:
	ciphertext = ''.join(f.read().split('\n'))
	ciphertext = binascii.a2b_base64(ciphertext)

def rate_key_size(key_size, ciphertext):
	dist = 0
	for block_1, block_2 in zip(chunks(ciphertext, key_size), chunks(ciphertext, key_size)[1:]):
		dist += hamming_distance(block_1, block_2)
	dist /=  len(ciphertext) / key_size
	normalized = dist / key_size
	return normalized

def recover_key(key_size, ciphertext):
	key = []
	for i in range(key_size):
		ct_part = ciphertext[i::key_size]
		char = recover_single_key(ct_part)
		key.append(char)
	key = bytes(key)
	return key
	
key_sizes = list(range(2, 41))
ranked_sizes = sorted(key_sizes, key=lambda ks: rate_key_size(ks, ciphertext))

key = recover_key(ranked_sizes[0], ciphertext)
decryption = repeating_xor(ciphertext, key)
print(key)
print(decryption)