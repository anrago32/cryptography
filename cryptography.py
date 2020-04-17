# Cryptography
# Basic cryptography implementation written in python
# Written by Antony Gordon, Alex Rago, Nick Rock, 2020

import random

# Euclidean algorithm for greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Algorithm to generate relatively prime public key
def generate_public_key(n, phi):
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    return e

# Extended euclidean algorithm for multiplicative inverse
def generate_private_key(e, phi):
    d, d_new = 0, 1
    r, r_new = phi, e
    while r_new > 0:
        a = r // r_new
        d, d_new = d_new, d - a * d_new
        r, r_new = r_new, r - a * r_new
    return d % phi

# Convert from string to ASCII
def fromString(sequence):
    sequence = [ord(c) for c in sequence]
    return sequence

# Convert to string from ASCII
def toString(sequence):
    sequence = [chr(c) for c in sequence]
    return "".join(sequence)

class Node():
    def __init__(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = generate_public_key(n, phi)
        d = generate_private_key(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

# Encode string with public key of recipient
def encrypt(recipient, sequence):
    (n, e) = recipient.public_key
    sequence = fromString(sequence)
    sequence = [(c ** e) % n for c in sequence]
    return sequence

# Decode with private key of recipient
def decrypt(recipient, sequence):
    (n, d) = recipient.private_key
    sequence = [(c ** d) % n for c in sequence]
    sequence = toString(sequence)
    return sequence

def main():
    # Using 8-bit primes
    alice = Node(211, 163)
    bob = Node(113, 199)

    message = "Hello, World!"
    print("Text Sent\t->\t" + message)
    message = encrypt(alice, message)
    print("Transmission\t->\t" + toString(message))
    message = decrypt(alice, message)
    print("Text Received\t->\t" + message)

    message = "Hello, Bob!"
    print("\nText Sent\t->\t" + message)
    message = encrypt(alice, message)
    print("Transmission\t->\t" + toString(message))
    message = decrypt(alice, message)
    print("Text Received\t->\t" + message)

if __name__ == "__main__":
    main()
