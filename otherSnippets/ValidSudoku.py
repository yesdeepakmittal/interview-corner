class Solution:
    def isValidSudoku(self, A):
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        squares = {(i,j):set() for i in range(3) for j in range(3)}  #need immutable key

        for row in range(9):
            for col in range(9):
                if A[row][col] == '.':
                    continue
                elif (A[row][col] in rows[row] or 
                    A[row][col] in cols[col] or
                    A[row][col] in squares[(row//3,col//3)]):
                    return 0
                else:
                    rows[row].add(A[row][col])
                    cols[col].add(A[row][col])
                    squares[(row//3,col//3)].add(A[row][col])
        return 1
print(Solution().isValidSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
                                 "7...2...6", ".6....28.", "...419..5", "....8..79"]))