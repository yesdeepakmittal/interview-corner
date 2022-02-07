'''
A = [1, 2, 3, 4, 5]
B = 5
o/p -> [2,3]

 A = [5, 10, 20, 100, 105]
 B = 110
 o/p -> [-1]

 A = [1,1000000]
 b = 1000000
 o/p = [1000000]
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # pf = [0]*len(A)
        # pf[0] = A[0]
        # for i in range(1,len(A)):
        #     pf[i] = pf[i-1] + A[i]
        # pf.insert(0,0)
        
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)+1):
        #         if pf[j] - pf[i] == B:
        #             return A[i:j]#[A[i],A[j-1]]
        # return [-1]
        
        i = 0
        j = 0
        s = 0

        while (i < len(A) and j < len(A)) or s >= B:
            if s < B:
                s += A[j]
                j += 1
            elif s > B:
                s -= A[i]
                i += 1
            else:
                return A[i:j]
        return [-1]

print(Solution().solve([1,100000],100000))