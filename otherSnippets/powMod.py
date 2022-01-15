class Solution:
    def pow(self, a,n,d):
        if a == 0:
            return 0
        if n == 0:
            return 1
        half_power = self.pow(a,n//2,d)
        if n%2 == 0:
            return (half_power * half_power) %d
        return (half_power*half_power*a) % d