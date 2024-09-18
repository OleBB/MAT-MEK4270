# for å sjekke åssen matrisen ser ut
import numpy as np
from scipy import sparse

class MyMatrixClass:
    def __init__(self, N, dx):
        self.N = N
        self.dx = dx

    def D2(self):
        D = sparse.diags([1, -2, 1], [-1, 0, 1], (self.N+1, self.N+1), 'lil')
        D[0, :4] = [2, -5, 4, -1]
        D[-1, -4:] = [-1, 4, -5, 2]
        D /= self.dx**2
        return D

# Example parameters
N = 5
dx = 0.1

# Create an instance of the class
matrix_instance = MyMatrixClass(N, dx)

# Generate the matrix D
D = matrix_instance.D2()

# Convert sparse matrix to dense format for better display
D_dense = D.toarray()

# Display the matrix
print(D_dense)
