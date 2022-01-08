''''
 A = [10, 5, 3, 4, 3, 5, 6] -> 5

 A = [6, 10, 5, 4, 9, 120] -> -1(No element found)
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d = {}
        ans = len(A) 
        for i in A:
            if i in d:
                if A.index(i) < ans:
                    ans = A.index(i)
                d[i] += 1
            else:
                d[i] = 1
        if ans == len(A):
            return -1 
        else:
            return A[ans]