class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        temp = sorted(list(set(A)))
        ans = []
        for i in temp:
            ans.append(d[i])
        return ans