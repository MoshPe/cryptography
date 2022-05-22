from Crypto.PublicKey import ElGamal
from os import urandom
import random
from el_gamal import elgamal
from salsa20 import salsa20

secret_key_Salsa20 = 0x8dbdc844531e223f6cb816e1eee4c0cb

nonce = 0xccc6f855277127780000000000000000
email_mgs = open("Email_message.txt", 'r').read()
# ciphertext = salsa20.encrypt_decrypt(salsa20, "Moshe peretz Tal-Chen Ben eliyahu Moshe peretz Tal-Chen Beneli", nonce, self.salsa20Key)
ciphertext = salsa20.encrypt_decrypt(salsa20, email_mgs, nonce, secret_key_Salsa20)
print(ciphertext)
plain = salsa20.encrypt_decrypt(salsa20, ciphertext, nonce, secret_key_Salsa20)
print(plain)
