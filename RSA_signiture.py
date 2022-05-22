import hashlib

from Crypto.PublicKey import ElGamal, RSA

def create_rsa_keys():
    rsa_key = RSA.generate(1024)
    private_key = int(rsa_key.exportKey('DER').hex(), 16)
    public_key = int(rsa_key.public_key().export_key('DER').hex(), 16)
    return private_key, public_key, rsa_key.n  # modulus

# TODO explain sha256
def create_rsa_signature(plaintext, private_key, modulo_n):
    hash = int.from_bytes(hashlib.sha256(plaintext.encode()).digest(), byteorder='big')
    signature = pow(hash, private_key, modulo_n)
    return hex(signature)


def verify_rsa_signature(signature, public_key, plaintext, modulo_n):
    hash_to_verify = int.from_bytes(hashlib.sha256(plaintext.encode()).digest(), byteorder='big')
    dec_signature = pow(int(signature, 16), public_key, modulo_n)
    if hash_to_verify == dec_signature:
        return True
    else:
        return False
