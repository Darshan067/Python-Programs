flat_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

size = int(len(flat_matrix) ** 0.5)
matrix = [flat_matrix[i*size:(i+1)*size] for i in range(size)]

diagonal = [matrix[i][i] for i in range(size)]
diagonal_sum = sum(diagonal)

print("Diagonal elements are:", diagonal)
print("Sum of diagonal elements =", diagonal_sum)
