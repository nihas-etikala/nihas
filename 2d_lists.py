matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# matrix[2][1] = 0
# print(matrix[2][1])
# print(matrix[1])
for row in matrix:
    for item in row:
        print(item)
    print(row)