class Solution:
    # @param A : string
    # @return an integer

    # TC - O(N2)
    def solve(self, a):
        ans = 0
        # for even length sub-string | baab
        for i in range(len(a)-1):
            ans = max(ans,self.expand(i,i+1,a))

        #for odd length sub-string  | bapab
        for i in range(len(a)):
            ans = max(ans,self.expand(i,i,a))
        return ans
    
    def expand(self,i,j,s):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt = j-i + 1
            i -= 1
            j += 1
        return cnt
