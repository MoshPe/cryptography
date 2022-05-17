import random
from Crypto.PublicKey import ElGamal
from os import urandom


class elgamal:

    # Bob receive from Alice p, g, e and encrypt the msg (- key ) and sent to Alice y1, y2
    def el_gamal_encryption(public_key_e, generator, modulo_p, msg):
        # generate random integer k
        k = random.randint(2, modulo_p - 1)

        # y1 = g^k mod p
        y1 = pow(generator, k, modulo_p)

        # y2 = M * e^k mod p
        y2 = (msg * pow(public_key_e, k)) % modulo_p
        return y1, y2


################################################################################
# # The decryptor - Alice:
# class the_decryptor:
#     # pre preparations: Alice choose p, g, d and calculate e and sent to the encryptor p,g,e
#     elgamal = ElGamal.generate(144, urandom)
#     elgamal_key = elgamal.publickey
#     # prime number p:
#     p = elgamal_key.__self__.p
#
#     # g when gcd(g,p)=1
#     g = elgamal_key.__self__.g
#
#     # generate random integer d between 2 to p-1
#     __d = random.randint(2, p - 1)
#
#     # calculate e = g^d mod p
#     e = pow(g, __d, p)
#
#     print("El gamal variables:")
#     print("p =",p ,"\n g =",g,"\n d =",__d, "\n e =",e,"\n")

    def el_gamal_decryption(self, y1, y2):
        # calculate (y1^d)^-
        y1_d_inv = pow(y1, self.__d, self.p)

        # plaintext = (y2 * (y1^d)^-1)) % modulo_p
        plaintext = (y2 * y1_d_inv) % self.p

        return plaintext
