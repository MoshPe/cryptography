from salsa20 import salsa20
# import Email_message

# hello I am Bob and I want to send an email to Alice
class encryptor:
    # Salsa20:
    private_key = '8dbdc844531e223f6cb816e1eee4c0cb'
    nonce = 0xccc6f85527712778
    block_number = 0x0000

    a0 = bytes(bytearray([101, 120, 112, 97]))
    a1 = bytes(bytearray([110, 100, 32, 49]))
    a2 = bytes(bytearray([54, 45, 98, 121]))
    a3 = bytes(bytearray([116, 101, 32, 107]))

    def __init__(self, key):
        self.key = key


    def encrypt_Salsa20(self, plaintext):
        print("hello encrypt_Salsa20")
        # covert the message to numbers
        encoded_message = plaintext.encode()

        # divide the encoded_message into blocks
        byte_array = bytearray(encoded_message)
        ciphertext = []
        for i in range(0, len(plaintext), 64):
            # print("type nonce", type(self.nonce), "||| type block number:", type(self.block_number))
            # print("typ n:", type(n),":: n=",n, "||| str n", str(n))
            print("nonce =",str(self.nonce),"block i =",str(self.block_number))
            print("ken block=",len(str(self.block_number)))
            # n = (self.nonce << 64) + self.block_number
            n = str(self.nonce) + str(self.block_number)
            print("n =", str(n))
            self.block_number += 1  # update the block number
            Ci = salsa20.ExmpansionFunction(salsa20, str(n), self.private_key)
            ciphertext.append(Ci)
            
            # we need to do XOR !!



# load the email message
email_mgs = open('Email_message.txt','r').read()
encryptor.encrypt_Salsa20(encryptor, email_mgs)




