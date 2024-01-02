# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        start = 0
        end = len(s) - 1

        return self.my_func(s, start, end)

    def my_func(self, s, start, end):
        if start > end:
            return True
        elif s[start] != s[end]:
            return False
        else:
            return self.my_func(s, start + 1, end - 1)