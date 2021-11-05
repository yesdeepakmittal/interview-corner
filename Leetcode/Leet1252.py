class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]*n for i in range(m)]
        for i in indices:
            indices_x, indices_y = i
            
            #for row increment - column will vary
            for col in range(n):
                matrix[indices_x][col] += 1
            
            #for column increment - row will vary
            for row in range(m):
                matrix[row][indices_y]  += 1
                
        #counting odd-valued cells in the matrix
        count = 0
            
        for row in range(m):
            for col in range(n):
                if matrix[row][col] % 2 != 0: count += 1
            
        return count
        