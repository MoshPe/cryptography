from el_gamal import elgamal
from Crypto.PublicKey import ElGamal
from salsa20 import salsa20
from os import urandom
import random
import RSA_signiture
from colorama import Fore, Style


# The decryptor - Alice:
class decryptor:   
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
    d = random.randint(2, p - 1)
    # d = 872362360549975597648220985046511570234990375919

    # calculate e = g^d mod p
    e = int(pow(g, d, p))
    # e = 539240174393814288124792318237250874564687333596

    def elgamal_publicVriables(self):
        return self.p, self.g, self.e

    ############### salsa20 ###############
    # hexkey = secrets.token_hex(16)
    # secret_key_Salsa20 = int(hexkey, 16)    
    nonce = 0xccc6f855277127780000000000000000 # maybe find function to generate the nunce?
    
    def decrypt_salsa20(self, ciphertext, y1, y2, DS, RSA_public_e, RSA_modulus_n, len_plaintext):
        # get the secret_key_Salsa20 
        secret_key_Salsa20 = elgamal.decryption_elgamal(elgamal, y1, y2, self.d, self.p)
        plaintext = salsa20.encrypt_decrypt(salsa20, ciphertext, self.nonce, secret_key_Salsa20)
        
        # check the DS:
        isVerified = RSA_signiture.verify_rsa_signature(DS, RSA_public_e, plaintext, RSA_modulus_n)
        print("\n*************************************")
        if isVerified:
            print("     Bob has been approved!!")
        else:
            print("     OSCAR BRIDGE THE SYSTEM!!")
        print("*************************************")
            
        # Remove the padding
        plaintext = plaintext[:len_plaintext]
        return plaintext
