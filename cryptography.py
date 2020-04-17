# Cryptography
# Basic cryptography implementation written in Python
# Written by Antony Gordon, Alex Rago, Nick Rock, 2020

import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_public_key(n, phi):
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    return e

def generate_private_key(e, phi):
    print("Not Defined")
    return 0

class Node():
    def __init__(p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = generate_public_key(n, phi)
        d = generate_private_key(e, phi)
        self.public_key = (n, e)
        self.private_key = (n, d)

    # Encode with private key of sender and then public key of recipient
    def encrypt(self, recipient, text):
        key1 = self.private_key
        key2 = recipient.public_key
        print("Not Defined")
        return text

    # Decode with private key of recipient and then public key of sender
    def decrypt(self, sender, text):
        key1 = self.private_key
        key2 = sender.public_key
        print("Not Defined")
        return text

def main():
    # Example Usage
    # p, q = ...
    # Alice = Node(p, q)
    # p, q = ...
    # Bob = Node(p, q)
    #
    # message = "Hello, World!"
    # message = Alice.encrypt(Bob, message)
    # message = Bob.decrypt(Alice, message)
    print()

if __name__ == "__main__":
    main()
