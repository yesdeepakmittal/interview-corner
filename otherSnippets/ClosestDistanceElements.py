''''
Closest distance b/t two elements which are repeating in an array

A = [7, 1, 3, 4, 1, 7] -> 3(for 1)
A = [1, 1] -> (for 1)
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        idx = 0
        d = {}
        ans = len(A)
        for i in A:
            if i in d:
                if d[i][1] == len(A):
                    d[i][1] = idx
                    # d[i][2] += 1
                else:
                    d[i][0] = d[i][1]
                    d[i][1] = idx
                    # d[i][2] += 1

                if d[i][1] - d[i][0] < ans:
                    ans = d[i][1] - d[i][0]
            else:
                d[i] = [idx,len(A)]  #[a index, b index, count of number]
            idx += 1
        
        if ans == len(A):
            return -1 
        else:
            return ans
