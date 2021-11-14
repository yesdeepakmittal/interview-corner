#https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = start + (end - start)//2
            if target < letters[mid]: # a < c - True
                end = mid - 1
            else:
                start = mid + 1
        return letters[start%len(letters)]