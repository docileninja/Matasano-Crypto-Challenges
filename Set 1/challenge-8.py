#! /usr/bin/python
# Challenge 8 - Detect AES in ECB mode

from utils import chunks
import binascii

with open("8.txt", 'r') as f:
	ciphertexts = []
	for line in f:
		ciphertexts.append(binascii.a2b_hex(line.strip()))

distinct_chunks = []
for ciphertext in ciphertexts:
	num_distinct = len(set(chunks(ciphertext, 8)))
	distinct_chunks.append((num_distinct, ciphertext))

print(min(distinct_chunks))