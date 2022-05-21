import random
from Crypto.PublicKey import ElGamal
from os import urandom


class elgamal:

    # Bob receive from Alice p, g, e and encrypt the msg (- key ) and sent to Alice y1, y2
    def encryption_elgamal(public_key_e, generator, modulo_p, msg):
        # generate random integer k
        # k = random.randint(2, modulo_p - 1)
        k = 13
    
        # y1 = g^k mod p
        y1 = pow(generator, k, modulo_p)

        # y2 = M * e^k mod p
        y2 = (msg * pow(public_key_e, k)) % modulo_p

        return y1, y2


    def decryption_elgamal(self, y1, y2):
        # calculate (y1^d)^-
        y1_d_inv = pow(y1, self.__d, self.p)

        # plaintext = (y2 * (y1^d)^-1)) % modulo_p
        plaintext = (y2 * y1_d_inv) % self.p

        return plaintext
