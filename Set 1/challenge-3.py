import binascii
from pprint import pprint
from utils import letter_frequencies, single_xor, rate_string

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte_string = binascii.a2b_hex(hex_string)

possible_decryptions = []
for i in range(256):
	possible_decryption = single_xor(byte_string, i)
	possible_decryptions.append(possible_decryption)

pprint(sorted(possible_decryptions, key=rate_string)[-1])