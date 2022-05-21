from el_gamal import elgamal
from Crypto.PublicKey import ElGamal
from salsa20 import salsa20
from os import urandom
import random
import secrets


# The decryptor - Alice:
class decryptor:
    # hexkey = secrets.token_hex(16)
    # secret_key_Salsa20 = int(hexkey, 16)

    secret_key_Salsa20 = 0x8dbdc844531e223f6cb816e1eee4c0cb
    
    
    ############### RSA ###############
    
    ############### elgamal ###############
    # pre prerequisite: Alice choose p, g, d and calculate e and sent to the encryptor p,g,e
    elgamal_variables = ElGamal.generate(161, urandom)
    elgamal_key = elgamal_variables.publickey
    
    # prime number p:
    p = int(elgamal_key.__self__.p)
    # p = 2521092666689958352506689839571798066901999312563

    # g when gcd(g,p)=1
    g = int(elgamal_key.__self__.g)
    # g = 2220446838505632479515696839173005671811547382699

    # generate random integer d between 2 to p-1
    __d = random.randint(2, p - 1)

    # calculate e = g^d mod p
    e = int(pow(g, __d, p))
    # e = 539240174393814288124792318237250874564687333596

    def elgamal_publicVriables(self):
        return self.p, self.g, self.e
    
    def encrypt_secret_key_Salsa20(self):
        
        return elgamal.encryption_elgamal(self.e, self.g, self.p, self.secret_key_Salsa20)
    

    ############### salsa20 ###############
    nonce = 0xccc6f855277127780000000000000000 # maybe find function to generate the nunce?
    def decrypt_salsa20(self, ciphertext):
       
        # def encrypt_decrypt(self, message, nonce, private_key):
       plaintext = salsa20.encrypt_decrypt(salsa20, ciphertext, self.nonce, self.secret_key_Salsa20)
       
       
       return plaintext