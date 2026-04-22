#caesar cipher encryption and decryption

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    """Encrypt text using Caesar cipher"""
    size = len(text)
    ciphertext = ""
    
    for i in range(size):
        char = text[i]
        if char in alpha:
            index = alpha.find(char)
            newindex = (index + key) % 26
            ciphertext += alpha[newindex]
        else:
            ciphertext += char
    
    return ciphertext

def decrypt(text, key):
    """Decrypt text using Caesar cipher"""
    size = len(text)
    plaintext = ""
    
    for i in range(size):
        char = text[i]
        if char in alpha:
            index = alpha.find(char)
            newindex = (index - key) % 26
            plaintext += alpha[newindex]
        else:
            plaintext += char
    
    return plaintext

# Main menu
print("=" * 40)
print("  CAESAR CIPHER - ENCRYPTION/DECRYPTION")
print("=" * 40)

choice = input("\nSelect an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice (1, 2, or 3): ")

match choice:
    case "1":
        plaintext = input("\nEnter your data (lowercase letters): ")
        key = int(input("Enter your key: "))
        result = encrypt(plaintext, key)
        print(f"\nOriginal Text: {plaintext}")
        print(f"Key: {key}")
        print(f"Encrypted Text: {result}")
    
    case "2":
        ciphertext = input("\nEnter encrypted data (lowercase letters): ")
        key = int(input("Enter your key: "))
        result = decrypt(ciphertext, key)
        print(f"\nEncrypted Text: {ciphertext}")
        print(f"Key: {key}")
        print(f"Decrypted Text: {result}")
    
    case "3":
        print("\nThank you for using Caesar Cipher!")
        exit()
    
    case _:
        print("\nInvalid choice! Please enter 1, 2, or 3.")