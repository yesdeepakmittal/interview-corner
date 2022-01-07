''''
i/p - Array of length >= 4 | o/p maximum &(bitwise) product of 4 numbers out of array
find maximum value of A[i] & A[j] & A[k] & A[l] where i,j,k,l are different indexes of array | &(bitwise AND)

 A = [10, 20, 15, 4, 14] 
 o/p -> 4 (20 & 15 & 4 & 15)

 A = [2, 2, 7, 15]
 o/p -> 2(2 & 2 & 7 & 15)
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        for i in range(30,-1,-1):
            x = 0
            for j in range(0,len(A)):
                if (A[j] & (1 << i)) > 0:
                    x += 1
            if x > 3:
                ans += 1 << i
                for j in range(0,len(A)):
                    if (A[j] & (1 << i)) == 0:
                        A[j] = 0
        return ans 