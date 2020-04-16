# Cryptography
# Basic cryptography implementation written in Python
# Written by Antony Gordon, Alex Rago, Nick Rock, 2020

class Node():
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def decrypt(self, sending_node, data):
        print("Not Defined")

    def encrypt(self, receiving_node, data):
        print("Not Defined")

    def get_public_key(self):
        return self.public_key

def main():
    print("Not Defined")

if __name__ == "__main__":
    main()
