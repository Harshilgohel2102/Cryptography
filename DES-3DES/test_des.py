from des import encrypt_message, decrypt_message

key = b"DESCRYPT"
msg = "hello"

ct = encrypt_message(key, msg)
pt = decrypt_message(key, ct)

assert pt == msg
print("DES test passed!")