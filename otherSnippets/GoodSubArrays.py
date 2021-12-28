''''
Good SubArray
-> length of subarray is even and sum of subarray < B
-> length of subarray is odd and sum of subarray > B
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cnt = 0
        for i in range(len(A)):
            s= 0
            for j in range(i,len(A)):
                s += A[j]
                
                if (j-i+1)%2 == 0 and s < B:
                    cnt += 1
                elif (j-i+1)%2 == 1 and s > B:
                    cnt += 1
        return cnt
