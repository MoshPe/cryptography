# from ElGamal import ElGamal
from salsa20 import salsa20
from os import urandom
import random



# The decryptor - Alice:
class decryptor:
    secret_key_Salsa20 = 0x8dbdc844531e223f6cb816e1eee4c0cb
    
    
    #RSA
    
    #elgamal
    
    # pre preparations: Alice choose p, g, d and calculate e and sent to the encryptor p,g,e
    # elgamal = ElGamal.generate(161, urandom)
    # elgamal_key = elgamal.publickey
    # # prime number p:
    # p = elgamal_key.__self__.p

    # # g when gcd(g,p)=1
    # g = elgamal_key.__self__.g

    # # generate random integer d between 2 to p-1
    # __d = random.randint(2, p - 1)

    # # calculate e = g^d mod p
    # e = pow(g, __d, p)

    # print("El gamal variables:")
    # print("p =",p ,"\n g =",g,"\n d =",__d, "\n e =",e,"\n")

    #salsa20
    nonce = 0xccc6f855277127780000000000000000 # maybe find function to generate the nunce?
    def decrypt_salsa20(self, ciphertext):
       
        # def encrypt_decrypt(self, message, nonce, private_key):
       plaintext = salsa20.encrypt_decrypt(salsa20, ciphertext, self.nonce, self.secret_key_Salsa20)
       
       
       return plaintext