https://leetcode.com/problems/set-matrix-zeroes/

matrix = [[1,1,0],[1,1,1],[1,1,1]]
idx = []
for row in range(len(matrix)):
    for index,value in enumerate(matrix[row]):
        if value == 0:
            matrix[row] = [0 for i in range(len(matrix[row]))]
            # for col in range(len(matrix)):
            #     matrix[col][index] = 0  does not work b'coz of running changes
                # print(matrix[col][index])
            idx.append(index)
for i in idx:
    for row in range(len(matrix)):
        matrix[row][i] = 0
print(matrix)
