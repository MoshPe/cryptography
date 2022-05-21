from salsa20 import salsa20
import numpy as np
# import Email_message

# hello I am Bob and I want to send an email to Alice
class encryptor:
    #RSA


    #elgamal
    salsa20Key = 0x8dbdc844531e223f6cb816e1eee4c0cb # will get it from elgamal
    
    
    # Salsa20:
    nonce = 0xccc6f855277127780000000000000000 # maybe find function to generate the nunce?
        
            
    def string_frombits(bits):
        chars = []
        for b in range(int(len(bits) / 8)):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)
    
    
    def encryptor_salsa20(self, filename2encrypt, nonce):
        # load the email message
        email_mgs = open(filename2encrypt,'r').read()
        
        # ciphertext = salsa20.encrypt_decrypt(salsa20, "Moshe peretz Tal-Chen Ben eliyahu Moshe peretz Tal-Chen Beneli", nonce, self.salsa20Key)
        ciphertext = salsa20.encrypt_decrypt(salsa20, email_mgs, nonce, self.salsa20Key)

        return ciphertext

        
        
        
        
# private_key = 0x8dbdc844531e223f6cb816e1eee4c0cb
# nonce = 0xccc6f855277127780000000000000000
# block_number = '0000000000000000'

# a0 = bytes(bytearray([101, 120, 112, 97]))
# a1 = bytes(bytearray([110, 100, 32, 49]))
# a2 = bytes(bytearray([54, 45, 98, 121]))
# a3 = bytes(bytearray([116, 101, 32, 107]))


# def __init__(self, key):
#     self.key = key

# def string_tobits(s):
#     result = []
#     for c in s:
#         bits = bin(ord(c))[2:]
#         bits = '00000000'[len(bits):] + bits
#         result.extend([int(b) for b in bits])
#     return result

# def string_frombits(bits):
#     chars = []
#     for b in range(int(len(bits) / 8)):
#         byte = bits[b*8:(b+1)*8]
#         chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
#     return ''.join(chars)



# def bitfield(n):
#     mestane = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
#     bits = bin(n)[2:]
#     array = []*32
#     for i in range(0, 32 - len(bits)):
#         mestane.insert(0, 0)

#     return mestane


# def flatten(self, matrix):
#     mat_bits = [self.bitfield(item) for sublist in matrix for item in sublist]
#     return [item for sublist in mat_bits for item in sublist]


# def XOR(array1, array2, num_bytes):
#     result = []
#     for i in range(0, num_bytes*8):
#         result.append(array1[i] ^ array2[i])
#     return result
    
# def encrypt_Salsa20(self, plaintext):
#     print("hello encrypt_Salsa20")
#     # covert the message to numbers
#     encoded_message = plaintext.encode()

#     # divide the encoded_message into blocks
#     byte_array = bytearray(encoded_message)
#     ciphertext = []
#     for i in range(0, len(plaintext), 64):
#         n = self.nonce
#         block = plaintext[i : i + 64]
#         block_bits = self.string_tobits(block)
      
#         Ci = salsa20.ExmpansionFunction(salsa20, n, self.private_key)
#         Ci_bits = self.flatten(self, Ci)

#         # XOR between the output fromExmpansionFunction -Ci_bits to the block of the plaintext- block_bits
#         resultXOR = self.XOR(Ci_bits, block_bits, 64)            
#         ciphertext.append(resultXOR)
        
#         # only for testing!!!!!!!!
#         # cipher = (self.XOR(Ci_bits, block_bits, 64))
#         # print("cipher:",self.string_frombits(cipher),"\n")
#         # print("plaintext:", self.string_frombits(self.XOR(Ci_bits, cipher, 64)) ,"\n")
        
#         n += 1  # update the block number
#     return ciphertext






    
