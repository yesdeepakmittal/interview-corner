class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        ans = []
        n = len(A)
        m = len(A[0])
        for k in range(m):
            i = 0
            j = k
            arr = []
            while i < n and j >= 0:
                arr.append(A[i][j])
                i += 1
                j -= 1
            ans.append(arr)
        for k in range(1,n):
            i = k
            j = m - 1
            arr = []
            while i < n and j >= 0:
                arr.append(A[i][j])
                i += 1
                j -= 1
            ans.append(arr)
        return ans