class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if mat == target: return True
            else:
                mat = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[-1])-1,-1,-1)]
        return False
        