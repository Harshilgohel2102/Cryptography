"""
WARNING:
Triple DES (3DES) is more secure than DES but still considered deprecated.
Use AES for modern secure systems.
This implementation is for educational and demonstration purposes only.
"""

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import sys

# -------------------------
# Key Generation
# -------------------------
def generate_key():
    while True:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        try:
            DES3.new(key, DES3.MODE_CBC)
            return key
        except ValueError:
            continue

# -------------------------
# Encryption
# -------------------------
def encrypt(message, key):
    cipher = DES3.new(key, DES3.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), DES3.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

# -------------------------
# Decryption
# -------------------------
def decrypt(ciphertext, key):
    raw = base64.b64decode(ciphertext)
    iv = raw[:8]
    ct = raw[8:]
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(ct), DES3.block_size)
    return decrypted.decode()

# -------------------------
# Input
# -------------------------
def get_message():
    msg = input("Enter message: ").strip()
    if not msg:
        print("Message cannot be empty")
        sys.exit()
    return msg

# -------------------------
# Menu
# -------------------------
def menu():
    print("===== Triple DES (3DES) Menu =====")
    print("1. Generate Key")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    key = None

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == '1':
            key = generate_key()
            print("Key (base64):", base64.b64encode(key).decode())

        elif choice == '2':
            if not key:
                print("Generate key first!")
                continue
            msg = get_message()
            ct = encrypt(msg, key)
            print("Encrypted:", ct)

        elif choice == '3':
            if not key:
                print("Generate key first!")
                continue
            ct = input("Enter ciphertext: ")
            try:
                pt = decrypt(ct, key)
                print("Decrypted:", pt)
            except Exception:
                print("Invalid ciphertext or key")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")