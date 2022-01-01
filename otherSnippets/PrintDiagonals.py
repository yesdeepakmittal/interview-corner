mat =  [[1,2,3,4,5],
        [1,2,3,4,5],
        [1,2,3,4,5],
        [1,2,3,4,5],
        [1,2,3,4,5]]
print('Diagonals from L to R')
for row in range(len(mat[0])):
    print(mat[row][row])

print('Diagonals from R to L')
row = 0
col = len(mat[0]) - 1
while row <= len(mat[0])-1 and col >= 0:
    print(mat[row][col])
    row += 1
    col -= 1