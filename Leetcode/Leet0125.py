class Solution:
    def isPalindrome(self, s: str) -> bool:
        var = ''

        for i in s:
            if i.isalnum():
                var += i.lower()

        return var == var[::-1]