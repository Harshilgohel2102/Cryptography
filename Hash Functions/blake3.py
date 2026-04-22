#importing " blake3 " library

from blake3 import blake3

# Take user input
data = input("Enter Your Data: ")

# Generate hash
hash_object = blake3(data.encode())

# Print hash (hex format)
print("BLAKE3 Hash:", hash_object.hexdigest())