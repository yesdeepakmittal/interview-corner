class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        n = str(A)
        arr = []
        for i in range(len(n)):
            for j in range(i+1,len(n)+1):
                arr.append(n[i:j])
        ans = set()
        for n in arr:
            temp = 1
            for i in n:
                temp *= int(i)
            if temp in ans:
                return 0
            else:
                ans.add(temp)
        return 1