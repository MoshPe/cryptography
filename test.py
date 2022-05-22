from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import RSA_signiture

# generate private/public key pair
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

# get public key in OpenSSH format
public_key = key.public_key().public_numbers()
print("public n", public_key.n)
print("public e",public_key.e)


# get private key in PEM container format
pem = key.private_numbers().d

hash = RSA_signiture.create_rsa_signature("Hello there", pem, public_key.n)
print(RSA_signiture.verify_rsa_signature(hash, public_key.e, "Hello there", public_key.n))

