from salsa20 import salsa20
from el_gamal import elgamal
import RSA_signiture
import secrets


# hello I am Bob and I want to send an email to Alice
class encryptor:
    email_msg = ""
   
    ############### RSA ###############
    RSA_private_d, RSA_public_e, RSA_modulus_n = RSA_signiture.create_rsa_keys()

    def RSA_publicVriables(self):
        return self.RSA_public_e, self.RSA_modulus_n

    def RSA_sign_request(self):
        return RSA_signiture.create_rsa_signature(self.email_msg, self.RSA_private_d, self.RSA_modulus_n)


    ############### elgamal ###############
    # keySize = 16
    # baseHex = 16
    # secret_key_Salsa20 = int(secrets.token_hex(keySize), baseHex)
    secret_key_Salsa20 = 0x8dbdc844531e223f6cb816e1eee4c0cb


    def encrypt_secret_key_Salsa20(self, e, g, p):
        # encrypt the secret key of salsa20 and return Y1, Y2
        return elgamal.encryption_elgamal(e, g, p, self.secret_key_Salsa20)


    ############### Salsa20 ###############
    nonce = 0xccc6f855277127780000000000000000 # maybe find function to generate the nunce?
        
    def string_frombits(bits):
        chars = []
        for b in range(int(len(bits) / 8)):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)
    
    
    def encryptor_salsa20(self, filename2encrypt, nonce):
        # load the email message
        self.email_msg = open(filename2encrypt,'r').read()
        len_plaintext = len(self.email_msg)
       
        # padding the message to be multiply of 64 bytes
        num_padding = 64 - (len(self.email_msg) % 64)
        if (len(self.email_msg) % 64 != 0):
            for i in range(0, num_padding):
                self.email_msg += "$"  # while space is using as padding

        ciphertext = salsa20.encrypt_decrypt(salsa20, self.email_msg, nonce, self.secret_key_Salsa20)

        return ciphertext, len_plaintext



    
