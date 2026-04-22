from des3 import encrypt, decrypt, generate_key

key = generate_key()
msg = "hello world"

ct = encrypt(msg, key)
pt = decrypt(ct, key)

assert pt == msg
print("3DES test passed!")