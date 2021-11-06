class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        arr = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                arr.append(True)
            else:
                arr.append(False)
        return arr
        