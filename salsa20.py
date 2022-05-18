import numpy

class salsa20:
    # for 16 bytes key
    a0 = bytes(bytearray([101, 120, 112, 97]))
    a1 = bytes(bytearray([110, 100, 32, 49]))
    a2 = bytes(bytearray([54, 45, 98, 121]))
    a3 = bytes(bytearray([116, 101, 32, 107]))
    # a0 = [101, 120, 112, 97]
    # a1 = [110, 100, 32, 49]
    # a2 = [54, 45, 98, 121]
    # a3 = [116, 101, 32, 107]

    # for 32 bytes key
    a0 = [101, 120, 112, 97]
    a1 = [110, 100, 32, 51]
    a2 = [50, 45, 98, 121]
    a3 = [116, 101, 32, 107]

    def XOR(self, num1, num2):
        return num1 ^ num2

    def QuarterRound_calculate(self, a, b, c, numShift):
        result = (b + c) % pow(2, 32)
        result_shiftLeft7 = result << numShift
        return self.XOR(a, result_shiftLeft7)

    def QuarterRound(self, y0, y1, y2, y3):
        z1 = self.QuarterRound_calculate(y1, y0, y3, 7)
        z2 = self.QuarterRound_calculate(y2, z1, y0, 9)
        z3 = self.QuarterRound_calculate(y3, z2, z1, 13)
        z0 = self.QuarterRound_calculate(y0, z3, z2, 18)

        return z0, z1, z2, z3

    def RowRound(self, y_matrix):
        (z0, z1, z2, z3) = self.QuarterRound(y_matrix[0][0], y_matrix[0][1], y_matrix[0][2], y_matrix[0][3])
        (z5, z6, z7, z4) = self.QuarterRound(y_matrix[1][1], y_matrix[1][2], y_matrix[1][3], y_matrix[1][0])
        (z10, z11, z8, z9) = self.QuarterRound(y_matrix[2][2], y_matrix[2][3], y_matrix[2][0], y_matrix[2][1])
        (z15, z12, z13, z14) = self.QuarterRound(y_matrix[3][3], y_matrix[3][0], y_matrix[3][1], y_matrix[3][2])

        result_matrix = [[z0, z1, z2, z3],
                         [z4, z5, z6, z7],
                         [z8, z9, z10, z11],
                         [z12, z13, z14, z15]]
        return result_matrix

    def ColumnRound(self, x_matrix):
        (y0, y4, y8, y12) = self.QuarterRound(x_matrix[0][0], x_matrix[1][0], x_matrix[2][0], x_matrix[3][0])
        (y5, y9, y13, y1) = self.QuarterRound(x_matrix[1][1], x_matrix[2][1], x_matrix[3][1], x_matrix[0][1])
        (y10, y14, y2, y6) = self.QuarterRound(x_matrix[2][2], x_matrix[3][2], x_matrix[0][2], x_matrix[1][2])
        (y15, y3, y7, y11) = self.QuarterRound(x_matrix[3][3], x_matrix[0][3], x_matrix[1][3], x_matrix[2][3])

        result_matrix = [[y0, y1, y2, y3],
                         [y4, y5, y6, y7],
                         [y8, y9, y10, y11],
                         [y12, y13, y14, y15]]
        return result_matrix

    def DoubleRound(self, x_matrix):
        result_matrix = self.RowRound(self.ColumnRound(x_matrix))
        return result_matrix
    
    
    def split_into_parts(number, n_parts):
        # number ='8dbdc844531e223f6cb816e1eee4c0cb'
        # n_parts = 8
        matrix = []
    
        for i in range (0, len(number), n_parts):
            matrix.append(number[i : i+n_parts])
        
        for i in range(len(matrix)):
            print("the matrix i: ", matrix[i])
            matrix[i] = int.from_bytes(bytes.fromhex(matrix[i]), "big")
        
        return matrix

    def SalsaHash16(self, a0, k1, a1, n, a2, k2, a3):
        # ai is equal to 4 bytes
        # n is equal to nunce+block_number = 8+8 = 16 bytes
        # k1 = k2 and is equal to 16 byte.
        
        # therefore, because the x_matrix is [4][4] and each cell is 4bytes, 
        # so we divide ki and n into 4 parts
        print("send k1")
        k1_array = self.split_into_parts(k1, 8)
        print("send k2")
        k2_array = self.split_into_parts(k2, 8)
        print("send n =", n)
        n_array = self.split_into_parts(n, 8)
        
        x_matrix = [[a0, k1_array[0], k1_array[1], k1_array[2]],
                    [k1_array[3], a1, n_array[0], n_array[1]],
                    [n_array[2], n_array[3], a2, k2_array[0]],
                    [k2_array[1],k2_array[2], k2_array[3], a3]]
        
        return self.DoubleRound(x_matrix)


    def ExmpansionFunction(self, n, k):
        return self.SalsaHash16(self, self.a0, k, self.a1, n, self.a2, k, self.a3)
    
    
    