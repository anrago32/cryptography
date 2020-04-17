# Cryptography
# Basic cryptography implementation written in python
# Written by Antony Gordon, Alex Rago, Nick Rock, 2020

import random

# Convert from string to ASCII
def fromString(string):
    string = [ord(c) for c in string]
    return string

# Convert to string from ASCII
def toString(string):
    string = [chr(c) for c in string]
    return "".join(string)

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

class Node():
    def __init__(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = generate_public_key(n, phi)
        d = generate_private_key(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    # Encode with private key of sender and then public key of recipient
    def encrypt(self, recipient, string):
        (n, e) = recipient.public_key
        string = fromString(string)
        string = [(c ** e) % n for c in string]
        return string

    # Decode with private key of recipient and then public key of sender
    def decrypt(self, sender, string):
        (n, d) = self.private_key
        string = [(c ** d) % n for c in string]
        string = toString(string)
        return string

def main():
    alice = Node(83, 67)
    bob = Node(41, 59)
    message = "Hello, World!"
    print("Text Sent\t->\t" + message)
    message = alice.encrypt(bob, message)
    print("Transmission\t->\t" + toString(message))
    message = bob.decrypt(alice, message)
    print("Text Received\t->\t" + message)

if __name__ == "__main__":
    main()
