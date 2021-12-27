class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        mx= max(A)
        ans =len(A)
        mn = min(A)
        if mx == mn:
            return 1
        for i in range(n):
            if A[i] == mx:
                for j in range(i+1,n):
                    if A[j] == mn:
                        ans = min(ans,j-i+1)
                        break
            elif A[i] == mn:
                for j in range(i+1,n):
                    if A[j] == mx:
                        ans = min(ans,j-i+1)
                        break
        return ans

print(Solution().solve([1,3,5,1,9,2,1]))