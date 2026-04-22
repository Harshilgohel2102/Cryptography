"""
WARNING: This implementation is for educational purposes only.
Not secure for real-world cryptographic use.
"""

from random import randint
import math
import sys

ENABLE_ANIMATION = False

# -------------------------
# Prime Check
# -------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# -------------------------
# Generate Prime
# -------------------------
def generate_prime():
    while True:
        num = randint(100, 500)
        if is_prime(num):
            return num

# -------------------------
# GCD
# -------------------------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# -------------------------
# Modular Inverse
# -------------------------
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, _ = egcd(e, phi)
    if g != 1:
        return None
    return x % phi

# -------------------------
# Key Generation
# -------------------------
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# -------------------------
# Encryption
# -------------------------
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# -------------------------
# Decryption
# -------------------------
def decrypt(cipher, private_key):
    d, n = private_key
    return ''.join(chr(pow(num, d, n)) for num in cipher)

# -------------------------
# Input Validation
# -------------------------
def get_message():
    message = input("Enter message: ").strip()
    if not message:
        print("Error: Message cannot be empty")
        sys.exit()
    return message

# -------------------------
# Menu
# -------------------------
def menu():
    print("\n===== RSA Algorithm Menu =====")
    print("1. Generate Keys")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Exit")

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    public_key = None
    private_key = None

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == '1':
            public_key, private_key = generate_keys()
            print("Public Key:", public_key)
            print("Private Key:", private_key)

        elif choice == '2':
            if not public_key:
                print("Generate keys first!")
                continue
            msg = get_message()
            encrypted = encrypt(msg, public_key)
            print("Encrypted:", encrypted)

        elif choice == '3':
            if not private_key:
                print("Generate keys first!")
                continue
            cipher = input("Enter encrypted list (comma-separated): ")
            cipher_list = list(map(int, cipher.split(',')))
            decrypted = decrypt(cipher_list, private_key)
            print("Decrypted:", decrypted)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")