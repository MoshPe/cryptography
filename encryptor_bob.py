import salsa20

# hello I am Bob and I want to send an email to Alice
class encryptor:
    # Salsa20:
    private_key =1
    nonce = 0xccc6f85527712778
    block_number = 0x0000

    a0 = bytes(bytearray([101, 120, 112, 97]))
    a1 = bytes(bytearray([110, 100, 32, 49]))
    a2 = bytes(bytearray([54, 45, 98, 121]))
    a3 = bytes(bytearray([116, 101, 32, 107]))

    def __init__(self, key):
        self.key = key

    # load the email message


    def encrypt_Salsa20(self, plaintext):
        # cover the message to numbers
        encoded_message = plaintext.encode()

        # divide the encoded_message into blocks
        byte_array = bytearray(encoded_message)
        salsa20HashResult = []
        for i in range(0, len(plaintext), 64):
            n = (self.nonce << 64) + self.block_number
            self.block_number += 1  # update the block number
            salsa20HashResult.append(salsa20.ExmpansionFunction(n, self.private_key))

