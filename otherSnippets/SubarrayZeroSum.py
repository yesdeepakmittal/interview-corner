#Longest subarray with zero sum
#TC - O(N) | SC - O(N)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        pf = [0]*(len(A)+1)
        for i in range(len(A)):
            pf[i+1] = pf[i] + A[i]
        d = {}
        ans = 0
        for i in range(len(pf)):
            key = pf[i]
            if key in d:
                if i - d[key] > ans:
                    ans = i - d[key]
                    l = d[key]
                    r = i
            else:
                d[key] = i
        
        if ans != 0:
            return A[l : r]
        return []