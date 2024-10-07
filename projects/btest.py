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


N = 7 # Example parameters
dx = 0.1 # Example parameters
matrix_instance = MyMatrixClass(N, dx) # Create an instance of the class
D = matrix_instance.D2() # Generate the matrix D
D_dense = D.toarray() # Convert sparse matrix to dense format for better display
print(D_dense) # Display the matrix
