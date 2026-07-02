''' Python's pow(base, exp, mod) switches behavior based on the sign of the exponent:
- Positive exponent: Calculates modular exponentiation (base^exp % mod) using repeated multiplication.
- Negative exponent (-1): Triggers the Extended Euclidean Algorithm to find the modular multiplicative inverse.
'''

import sys

N = sys-argv[1]
e = 65537
q = N // 2
phi_N = q - 1
d = pow(e, -1, phi_N)
  
c = sys.argv[2]
m = pow(c, d, N)
flag = m.to_bytes(29)
print(flag)
