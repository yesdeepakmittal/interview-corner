class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        if n <= 1:
            return n
        nearest2power = self.nearest2power(n)
        bits_till_2_power = (1 << (nearest2power - 1))*nearest2power  # x.2**(x-1)
        msb_after_2_power_to_n = n - (1 << nearest2power) + 1# n - 2**x + 1
        remaining_bits_after2power_without_msb = n - (1 << nearest2power)
        ans = bits_till_2_power + msb_after_2_power_to_n + self.countSetBits(remaining_bits_after2power_without_msb)
        return ans
        
    def nearest2power(self,n):
        x = 0
        while (1 << x) <= n:
            x += 1
        return x - 1

print(Solution().countSetBits(51))