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
        encrypted_text = []
        for character in text:
            encrypted_character = (ord(character) ** e) % n
            encrypted_text.append(encrypted_character)
        return encrypted_text

    # Decode with private key of recipient and then public key of sender
    def decrypt(self, sender, encrypted_text):
        (n, d) = self.private_key
        text = ""
        for encrypted_character in encrypted_text:
            character = chr((encrypted_character ** d) % n)
            text += character
        return text

def main():
    alice = Node(83, 67)
    bob = Node(41, 59)
    message = "Hello, World!"
    print("Text Sent: " + message)
    message = alice.encrypt(bob, message)
    print("Transmission: " + str(message))
    message = bob.decrypt(alice, message)
    print("Text Received: " + message)

if __name__ == "__main__":
    main()
