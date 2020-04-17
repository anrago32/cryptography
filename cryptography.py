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

class Node():
    def __init__(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = generate_public_key(n, phi)
        d = generate_private_key(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    # Encode with private key of sender and then public key of recipient
    def encrypt(self, recipient, text):
        (n, e) = recipient.public_key
        text = (text ** e) % n
        return text

    # Decode with private key of recipient and then public key of sender
    def decrypt(self, sender, text):
        (n, d) = self.private_key
        text = (text ** d) % n
        return text

def main():
    alice = Node(83, 67)
    bob = Node(41, 59)

    message = 5
    message = alice.encrypt(bob, message)
    message = bob.decrypt(alice, message)
    print(message)

if __name__ == "__main__":
    main()
