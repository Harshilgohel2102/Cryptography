"""
WARNING: This DES implementation uses a legacy algorithm (DES) which is
considered insecure for modern applications. Use AES for real-world security.
This project is for educational purposes only.
"""

from pyDes import des, ECB, PAD_PKCS5
import sys

# -------------------------
# Key Setup
# -------------------------
def get_key():
    key_input = input("Enter 8-character key: ").strip()
    if len(key_input) != 8:
        print("Error: Key must be exactly 8 characters for DES")
        sys.exit()
    return key_input.encode()

# -------------------------
# Message Input
# -------------------------
def get_message():
    msg = input("Enter message: ").strip()
    if not msg:
        print("Error: Message cannot be empty")
        sys.exit()
    return msg

# -------------------------
# Encryption
# -------------------------
def encrypt_message(key, message):
    cipher = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(message)
    return encrypted

# -------------------------
# Decryption
# -------------------------
def decrypt_message(key, ciphertext):
    cipher = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()

# -------------------------
# Menu
# -------------------------
def menu():
    print("===== DES Algorithm Menu =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    key = get_key()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == '1':
            msg = get_message()
            ct = encrypt_message(key, msg)
            print("Encrypted (bytes):", ct)
            print("Encrypted (hex):", ct.hex())

        elif choice == '2':
            hex_input = input("Enter ciphertext (hex): ").strip()
            try:
                ct = bytes.fromhex(hex_input)
            except ValueError:
                print("Invalid hex input")
                continue

            pt = decrypt_message(key, ct)
            print("Decrypted:", pt)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")