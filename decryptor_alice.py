from ElGamal import ElGamal
from salsa20 import salsa20
from os import urandom


# The decryptor - Alice:
class decryptor:
    # pre preparations: Alice choose p, g, d and calculate e and sent to the encryptor p,g,e
    elgamal = ElGamal.generate(161, urandom)
    elgamal_key = elgamal.publickey
    # prime number p:
    p = elgamal_key.__self__.p

    # g when gcd(g,p)=1
    g = elgamal_key.__self__.g

    # generate random integer d between 2 to p-1
    __d = random.randint(2, p - 1)

    # calculate e = g^d mod p
    e = pow(g, __d, p)

    print("El gamal variables:")
    print("p =",p ,"\n g =",g,"\n d =",__d, "\n e =",e,"\n")


    def decrypt_Salsa20(self, plaintext):
        print("hello decrypt_Salsa20")
        # covert the message to numbers
        encoded_message = ciphertext.encode()
    
        # divide the encoded_message into blocks
        byte_array = bytearray(encoded_message)
        plaintext = []
        for i in range(0, len(ciphertext), 64):
            n = self.nonce
            block = ciphertext[i : i + 64]
            block_bits = self.string_tobits(block)
          
            Ci = salsa20.ExmpansionFunction(salsa20, n, self.private_key)
            Ci_bits = self.flatten(self, Ci)
    
            # XOR between the output fromExmpansionFunction -Ci_bits to the block of the ciphertext- block_bits
            resultXOR = self.XOR(Ci_bits, block_bits, 64)            
            plaintext.append(resultXOR)
            
            # only for testing!!!!!!!!
            # cipher = (self.XOR(c, block_bits, 64))
            # print("cipher:",self.string_frombits(cipher),"\n")
            # print("ciphertext:", self.string_frombits(self.XOR(c, cipher, 64)) ,"\n")
            
            n += 1  # update the block number
        return plaintext