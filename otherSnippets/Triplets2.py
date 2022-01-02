'''
Christmas Tree 
A = [size of tree]; B = [cost of each tree]
find minimum cost of trees such that A[i]<A[j]<A[k] and cost is minimum

TC - O(N2) | SC - O(1)
'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):        
        def left_count(i,A,B):
            flag = False
            MinB = max(B)
            for x in range(0,i):
                if A[x] < A[i]:
                    flag = True
                    if B[x] < MinB:
                        MinB = B[x]
            if flag:
                return MinB
            else:
                return -1
        def right_count(i,A,B):
            flag = False
            MinB = max(B)
            for x in range(i+1,len(A)):
                if A[x] > A[i]:
                    flag = True
                    if B[x] < MinB:
                        MinB = B[x]
            if flag:
                return MinB
            else:
                return -1
        s = 0
        ans = max(B)*3
        for i in range(1,len(A)-1):
            left = left_count(i,A,B)
            right = right_count(i,A,B)
            if left != -1 and right != -1:
                s = left + B[i] + right
                if s < ans:
                    ans = s

        if s != 0:
            return ans
        else:
            return -1
