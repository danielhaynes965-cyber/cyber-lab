# multistage decode - brute force caeser cipher -> base16 decode via binary converserion

import string

enc = 'fegdeogdgecoeocgcgchcfcffccfca'

alphabet = string.ascii_lowercase[0:16]

potential_keys = alphabet
    

def unshift(ch, key):
    original_ord = ord(ch) - ord('a')
    ord_shift = ord(key) - ord('a')
    return alphabet[(original_ord - ord_shift) % len(alphabet)]



def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += alphabet[int(binary[:4], 2)]
		enc += alphabet[int(binary[4:], 2)]
	return enc

def b16_decode(b16):
    plain = ""
    for i in range(0, len(b16), 2):
        binary = '{0:04b}'.format(alphabet.index(b16[i]))
        binary += '{0:04b}'.format(alphabet.index(b16[i+1]))
        plain += chr(int(binary, 2))    
    return plain
    
def main():

    for key in potential_keys:

        b16 = ""

        for ch in enc:
            b16 += unshift(ch, key)  

        plain = b16_decode(b16)

        print(plain)
        
main() 
