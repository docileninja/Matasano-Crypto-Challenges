import binascii

def xor_fixed(b1, b2):
	return bytes(c1 ^ c2 for c1, c2 in zip(b1, b2))

hex_string_one = '1c0111001f010100061a024b53535009181c'
hex_string_two = '686974207468652062756c6c277320657965'
bytes_one = binascii.a2b_hex(hex_string_one)
bytes_two = binascii.a2b_hex(hex_string_two)

print(xor_fixed(bytes_one, bytes_two))