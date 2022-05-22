import random
from Crypto.PublicKey import ElGamal
from os import urandom


class elgamal:

    # Bob receive from Alice p, g, e and encrypt the msg (- key ) and sent to Alice y1, y2
    def encryption_elgamal(public_key_e, generator, modulo_p, msg):
        # generate random integer k
        k = random.randint(2, modulo_p - 1)
        # y1 = g^k mod p
        s = pow(public_key_e, k, modulo_p)

        y1 = pow(generator, k, modulo_p)
        # y2 = M * e^k mod p
        y2 = (msg * s) % modulo_p

        return y1, y2


    def decryption_elgamal(self, y1, y2, d, p):
        # calculate (y1^d)^-
        y1_d_inv = pow(y1, d, p)
        y1_inv = pow(y1_d_inv, -1, p)
        # plaintext = (y2 * (y1^d)^-1)) % modulo_p
        plaintext = (y2 * y1_inv) % p

        return plaintext
