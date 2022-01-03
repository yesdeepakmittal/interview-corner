'''
A = [1,2] : Amount of gas available at station A
B = [2,1] : Amount of gas required to move from A[i] to A[j]
You can travel only in one direction
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        start = 0
        total_fuel = 0
        current_fuel = 0
        
        for index in range(len(A)):
            temp = A[index] - B[index]
            current_fuel =current_fuel + temp
            total_fuel = total_fuel+temp
            if current_fuel < 0:
                start = index + 1
                current_fuel = 0
        if total_fuel >= 0: return start
        return -1
