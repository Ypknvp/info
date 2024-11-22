from math import gcd
from sympy import mod_inverse

# Input prime numbers and the message
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
msg = int(input(f"Enter the message to encrypt (integer < {p*q}): "))

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Find e (public key exponent)
e = next(e for e in range(2, phi) if gcd(e, phi) == 1)

# Find d (private key exponent)
d = mod_inverse(e, phi)

# Encrypt the message
c = pow(msg, e, n)

# Decrypt the message
m = pow(c, d, n)

# Display results
print("\nRSA Key Details:")
print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")
print("\nResults:")
print(f"Encrypted message: {c}")
print(f"Decrypted message: {m}")