def determinant(matrix):
    det = (matrix[0][0]*matrix[1][1]*matrix[2][2] 
         + matrix[0][1]*matrix[1][2]*matrix[2][0] 
         + matrix[0][2]*matrix[1][0]*matrix[2][1] 
         - matrix[0][2]*matrix[1][1]*matrix[2][0] 
         - matrix[0][1]*matrix[1][0]*matrix[2][2] 
         - matrix[0][0]*matrix[1][2]*matrix[2][1])
    return det

matrix = [[-1, 1, 4], [3, 0, 2], [1, 3, -5]]
det = determinant(matrix)
print("Determinant:", det)