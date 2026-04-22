from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import binascii

def encrypt(data, key):
    """Encrypt data using AES-256 in CFB mode"""
    try:
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(data)
        return cipher.iv, ciphertext
    except Exception as e:
        print(f"Encryption error: {e}")
        return None, None

def decrypt(iv, ciphertext, key):
    """Decrypt data using AES-256 in CFB mode"""
    try:
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

def derive_key(password):
    """Derive a 32-byte key from a password using PBKDF2"""
    salt = b'aes_salt_2026'  # Fixed salt for consistency
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    return key

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("AES Encryption/Decryption Tool")
    print("="*50)
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Generate Random Key")
    print("4. Exit")
    print("="*50)

def encrypt_option():
    """Handle encryption option"""
    print("\n--- Encryption Mode ---")
    use_password = input("Do you want to use a password (y/n)? ").lower().strip()
    
    if use_password == 'y':
        password = input("Enter password: ")
        key = derive_key(password.encode('utf-8'))
    else:
        key = get_random_bytes(32)
        print(f"Generated key (hex): {binascii.hexlify(key).decode()}")
    
    plaintext = input("Enter text to encrypt: ")
    data = plaintext.encode('utf-8')
    
    iv, ciphertext = encrypt(data, key)
    if ciphertext:
        print(f"\nEncryption successful!")
        print(f"IV (hex): {binascii.hexlify(iv).decode()}")
        print(f"Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}")
        
        if use_password != 'y':
            print(f"Key (hex): {binascii.hexlify(key).decode()}")

def decrypt_option():
    """Handle decryption option"""
    print("\n--- Decryption Mode ---")
    
    use_password = input("Do you want to use a password (y/n)? ").lower().strip()
    
    if use_password == 'y':
        password = input("Enter password: ")
        key = derive_key(password.encode('utf-8'))
    else:
        key_hex = input("Enter key (hex): ").strip()
        try:
            key = binascii.unhexlify(key_hex)
        except ValueError:
            print("Invalid hex format for key!")
            return
    
    iv_hex = input("Enter IV (hex): ").strip()
    ciphertext_hex = input("Enter ciphertext (hex): ").strip()
    
    try:
        iv = binascii.unhexlify(iv_hex)
        ciphertext = binascii.unhexlify(ciphertext_hex)
    except ValueError:
        print("Invalid hex format for IV or ciphertext!")
        return
    
    plaintext = decrypt(iv, ciphertext, key)
    if plaintext:
        print(f"\nDecryption successful!")
        print(f"Plaintext: {plaintext.decode('utf-8')}")

def generate_key_option():
    """Handle key generation option"""
    print("\n--- Key Generation ---")
    key = get_random_bytes(32)
    print(f"Generated AES-256 key (hex): {binascii.hexlify(key).decode()}")

def main():
    """Main function with switch case menu"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        # Switch case using dictionary
        switch = {
            '1': encrypt_option,
            '2': decrypt_option,
            '3': generate_key_option,
            '4': lambda: print("Exiting... Goodbye!")
        }
        
        action = switch.get(choice)
        
        if action:
            action()
            if choice == '4':
                break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()