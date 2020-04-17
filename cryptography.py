# Cryptography
# Basic RSA Implementation Written in Python
# Written by Antony Gordon, Alex Rago, Nick Rock, 2020

from random import randrange

# Simulated network node
class Node():
    def __init__(self, name, p, q):
        n, phi = p * q, (p - 1) * (q - 1)
        e = generate_public_key(n, phi)
        d = generate_private_key(e, phi)
        self.name = name
        self.public_key = (n, e)
        self.private_key = (n, d)

# Euclidean algorithm for greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Algorithm to generate relatively prime public key
def generate_public_key(n, phi):
    e = randrange(1, phi)
    while gcd(e, phi) != 1:
        e = randrange(1, phi)
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
def from_string(sequence):
    sequence = [ord(c) for c in sequence]
    return sequence

# Convert to string from ASCII
def to_string(sequence):
    sequence = [chr(c) for c in sequence]
    return "".join(sequence)

# Encode with public key of recipient
def encrypt(sequence, recipient):
    (n, e) = recipient.public_key
    sequence = [(c ** e) % n for c in sequence]
    return sequence

# Decode with private key of recipient
def decrypt(sequence, recipient):
    (n, d) = recipient.private_key
    sequence = [(c ** d) % n for c in sequence]
    return sequence

# Simulate encrypted network transmission
def simulate_transmission(message, recipient):
    print("\n>> \"" + message + "\" sent to " + recipient.name + "\n")
    message = from_string(message)
    print("\tOriginal Sequence:\n\t" + str(message))
    message = encrypt(message, recipient)
    print("\tEncrypted Sequence:\n\t" + str(message) + "\n")
    print(">> Encrypted Sequence Transmitted\n")
    print("\tReceived Sequence:\n\t" + str(message))
    message = decrypt(message, recipient)
    print("\tDecrypted Sequence:\n\t" + str(message) + "\n")
    message = to_string(message)
    print(">> \"" + message + "\" received by " + recipient.name + "\n")

def main():
    # Nodes with 8-bit primes
    node1 = Node("Alice", 211, 163)
    node2 = Node("Bob", 113, 199)

    # Simulated transmissions
    simulate_transmission("Hello, World!", node1)
    simulate_transmission("Secret Message", node2)

if __name__ == "__main__":
    main()
