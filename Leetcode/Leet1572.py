class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        p = 0
        s = 0
        length = len(mat)
        for i in range(length):
            p += mat[i][i]  #adding elements of primary diagonal
            s += mat[i][length - 1 - i] #adding elements of secondary diagonal
        
        #matrix with even dimension
        if length%2 == 0:
            return p+s
        
        #matrix with odd dimension
        else:
            #subtracting centered element which added twice
            return p + s - mat[int(length/2)][int(length/2)]  
        