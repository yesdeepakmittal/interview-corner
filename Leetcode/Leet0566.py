class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        for i in mat:
            arr += i
        if r*c == len(arr):
            i = 0
            ans = []
            for row in range(r):
                temp = []
                for col in range(c):
                    temp.append(arr[i + col])
                i += c
                ans.append(temp)
            return ans
        else: return mat
        