#https://practice.geeksforgeeks.org/problems/equal-sum-and-xor/1/
def countValues(n):
    # Code here
    cnt = 0
    for i in range(n+1):
        temp = i + n
        if temp == (n ^ i):
            cnt += 1
    return cnt