
class salsa20:
    # for 16 bytes key
    a0 = int.from_bytes(bytearray([101, 120, 112, 97]), "big")
    a1 = int.from_bytes(bytearray([110, 100, 32, 49]), "big")
    a2 = int.from_bytes(bytearray([54, 45, 98, 121]), "big")
    a3 = int.from_bytes(bytearray([116, 101, 32, 107]), "big")

    # for 32 bytes key
    # a0 = [101, 120, 112, 97]
    # a1 = [110, 100, 32, 51]
    # a2 = [50, 45, 98, 121]
    # a3 = [116, 101, 32, 107]

    def XOR_numbers(self, num1, num2):
        return num1 ^ num2
             
    
    def QuarterRound_calculate(self, a, b, c, numShift):
        result = (b + c) % pow(2, 32)
        result_shiftLeft7 = (pow(2, numShift) * result) % (pow(2, 32) - 1)
        return self.XOR_numbers(self, a, result_shiftLeft7)


    def QuarterRound(self, y0, y1, y2, y3):
        z1 = self.QuarterRound_calculate(self, y1, y0, y3, 7)
        z2 = self.QuarterRound_calculate(self, y2, z1, y0, 9)
        z3 = self.QuarterRound_calculate(self, y3, z2, z1, 13)
        z0 = self.QuarterRound_calculate(self, y0, z3, z2, 18)
        return z0, z1, z2, z3


    def RowRound(self, y_matrix):
        (z0, z1, z2, z3) = self.QuarterRound(self, y_matrix[0][0], y_matrix[0][1], y_matrix[0][2], y_matrix[0][3])
        (z5, z6, z7, z4) = self.QuarterRound(self, y_matrix[1][1], y_matrix[1][2], y_matrix[1][3], y_matrix[1][0])
        (z10, z11, z8, z9) = self.QuarterRound(self, y_matrix[2][2], y_matrix[2][3], y_matrix[2][0], y_matrix[2][1])
        (z15, z12, z13, z14) = self.QuarterRound(self, y_matrix[3][3], y_matrix[3][0], y_matrix[3][1], y_matrix[3][2])
        
        result_matrix = [[z0, z1, z2, z3],
                         [z4, z5, z6, z7],
                         [z8, z9, z10, z11],
                         [z12, z13, z14, z15]]
        return result_matrix


    def ColumnRound(self, x_matrix):
        (y0, y4, y8, y12) = self.QuarterRound(self, x_matrix[0][0], x_matrix[1][0], x_matrix[2][0], x_matrix[3][0])
        (y5, y9, y13, y1) = self.QuarterRound(self, x_matrix[1][1], x_matrix[2][1], x_matrix[3][1], x_matrix[0][1])
        (y10, y14, y2, y6) = self.QuarterRound(self, x_matrix[2][2], x_matrix[3][2], x_matrix[0][2], x_matrix[1][2])
        (y15, y3, y7, y11) = self.QuarterRound(self, x_matrix[3][3], x_matrix[0][3], x_matrix[1][3], x_matrix[2][3])

        result_matrix = [[y0, y1, y2, y3],
                         [y4, y5, y6, y7],
                         [y8, y9, y10, y11],
                         [y12, y13, y14, y15]]
        return result_matrix


    def DoubleRound(self, x_matrix):
        result_matrix = self.RowRound(self, self.ColumnRound(self, x_matrix))
        return result_matrix
    
    
    def split_into_parts(string, n_parts):
        matrix = []
        for i in range (0, len((string)), n_parts):
            matrix.append(string[i : i+n_parts])
        
        for i in range(len(matrix)):
            matrix[i] = int.from_bytes(bytes.fromhex(matrix[i]), "big")
        
        return matrix

    def SalsaHash16(self, a0, k1, a1, n, a2, k2, a3):
        # a_i is equal to 4 bytes
        # n is equal to nunce+block_number = 8+8 = 16 bytes
        # k1 = k2 and is equal to 16 byte.
        
        # therefore, because the x_matrix is [4][4] and each cell is 4 bytes, 
        # then we divide ki and n into 4 parts
        
        k1_array = self.split_into_parts(hex(k1)[2:], 8)
        k2_array = self.split_into_parts(hex(k2)[2:], 8)
        n_array = self.split_into_parts(hex(n)[2:], 8)
        
        x_matrix = [[a0, k1_array[0], k1_array[1], k1_array[2]],
                    [k1_array[3], a1, n_array[0], n_array[1]],
                    [n_array[2], n_array[3], a2, k2_array[0]],
                    [k2_array[1],k2_array[2], k2_array[3], a3]]
        
        result_matrixLopp = x_matrix
        for i in range(0, 10):
            result_matrixLopp = self.DoubleRound(self, result_matrixLopp)
        
        return result_matrixLopp



    def ExmpansionFunction16(self, n, k):
        return self.SalsaHash16(self, self.a0, k, self.a1, n, self.a2, k, self.a3)
    
    def encrypt_decrypt(self, message, nonce, private_key):
        # divide the encoded_message into blocks
        outpuText = []
        
        for i in range(0, len(message), 64):
            block = message[i : i + 64]
            block_bits = self.string_tobits(block)
          
            Ci = self.ExmpansionFunction16(self, nonce, private_key)
            Ci_bits = self.flatten(self, Ci)

            # XOR between the output fromExmpansionFunction -Ci_bits to the block of the message- block_bits
            resultXOR = self.XOR_array(Ci_bits, block_bits, 64)            
            outpuText.append(self.string_frombits(resultXOR))
            
            nonce += 1  # update the block number
            
        return ''.join(outpuText)
    
    ############################################################
    ########### Support function to encrypt & decrypt ###########
    ############################################################
    def string_tobits(s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    def string_frombits(bits):
        chars = []
        for b in range(int(len(bits) / 8)):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)
    
    
    
    def bitfield(n):
        mestane = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
        bits = bin(n)[2:]
        for i in range(0, 32 - len(bits)):
            mestane.insert(0, 0)

        return mestane


    def flatten(self, matrix):
        mat_bits = [self.bitfield(item) for sublist in matrix for item in sublist]
        return [item for sublist in mat_bits for item in sublist]
    
    
    def XOR_array(array1, array2, num_bytes):
        result = []
        for i in range(0, num_bytes*8):
            result.append(array1[i] ^ array2[i])
        return result
    


    