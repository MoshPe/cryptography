import ast
import hashlib


def create_rsa_signature(msg, private_key, modulo_n):
    hash = int.from_bytes(hashlib.sha256(msg).digest(), byteorder='big')
    signature = pow(hash, private_key, modulo_n)
    return hex(signature)


def verify_rsa_signature(hash, public_key, msg, modulo_n):
    hash_to_verify = int.from_bytes(hashlib.sha256(msg).digest(), byteorder='big')
    dec_signature = pow(int(hash, 16), public_key, modulo_n)
    if hash_to_verify == dec_signature:
        return True
    else:
        return False
