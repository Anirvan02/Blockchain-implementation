import hashlib

def find_nonce(s):
    nonce = 0
    while True:
        data = s + str(nonce)
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value.startswith('00'):
            print(f"Nonce found: {nonce}")
            print(f"Hash: {hash_value}")
            return nonce, hash_value
        nonce += 1

def verify_nonce(s, nonce):
    data = s + str(nonce)
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    return hash_value.startswith('00')

s = "block_data"
nonce, hash_value = find_nonce(s)

is_valid = verify_nonce(s, nonce)
print(f"Verification result: {is_valid}")