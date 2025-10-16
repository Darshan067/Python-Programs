import numpy as np

A = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

B = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

C = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

result = np.matmul(np.matmul(A, B), C)

print("Multiplication of the matrix:")
for row in result:
    print(*row)
