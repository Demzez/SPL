def showMatrix(matrix, rows, cols):
    print("Ваш массив:")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()


print("Введите размеры массива(rows, cols):")
rows, cols = input().split()
rows = int(rows)
cols = int(cols)

print("Введите массив:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

showMatrix(matrix,rows,cols)

print("Введите номера столбцов для замены(col1, col2):")
col1, col2 = input().split()
col1 = int(col1)-1
col2 = int(col2)-1
for row in matrix: row[col1], row[col2] = row[col2], row[col1]

showMatrix(matrix,rows,cols)


