import hashlib

plaintext = input("Enter Your Data: ")

hash_object = hashlib.sha256(plaintext.encode())

print("SHA-256 Hash:", hash_object.hexdigest())