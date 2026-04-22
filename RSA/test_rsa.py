from rsa import is_prime, gcd

# Basic Tests
assert is_prime(7) == True
assert is_prime(10) == False
assert gcd(10, 5) == 5

print("All tests passed!")