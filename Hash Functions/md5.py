import hashlib

plaintext = input("Enter Your Data: ")

# Convert input to bytes
encoded_data = plaintext.encode()

# Create MD5 hash
result = hashlib.md5(encoded_data)

# Print readable hash
print("MD5 Hash:", result.hexdigest())