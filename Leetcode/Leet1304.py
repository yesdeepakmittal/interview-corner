class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2 == 0:
            a = []
            for i in range(1,n//2+1):
                a.append(i)
                a.insert(0,-i)
        else: #odd
            a = [0]
            for i in range(1,n//2+1):
                a.append(i)
                a.insert(0,-i)
        return a