import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def create_rsa_keys():
    # generate private, public key
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
                                   key_size=2048)
    
    public_key = key.public_key().public_numbers()
    private_key = key.private_numbers().d
    return private_key, public_key.e, public_key.n  # modulus

def create_rsa_signature(plaintext, private_key, modulo_n):
    hashResult = int.from_bytes(hashlib.sha256(plaintext.encode()).digest(), byteorder='big')
    signature = pow(hashResult, private_key, modulo_n)
    return hex(signature)


def verify_rsa_signature(signature, public_key_e, plaintext, modulo_n):
    hash_to_verify = int.from_bytes(hashlib.sha256(plaintext.encode()).digest(), byteorder='big')
    dec_signature = pow(int(signature, 16), public_key_e, modulo_n)
    if hash_to_verify == dec_signature:
        return True
    else:
        return False
