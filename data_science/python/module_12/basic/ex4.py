"""
w3resource.com homework 
Basic #4

Author: Evert Ball
Version: 18 August 2020
"""
import numpy as np
from scipy import sparse

eye = np.eye(4)
print("NumPy array:")
print(eye)

sparse_matrix = sparse.csr_matrix(eye)
print("SciPy Sparse CSR Matrix:")
print(sparse_matrix)
