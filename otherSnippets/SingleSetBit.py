''''
Count how many set bits are present.
Return True if count is 1 else False
TC - O(log2N)
'''
def single_set(n):
    cnt = 0
    while n>0:
        c = n%2
        n //= 2   # n>>1
        if c == 1:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

print(single_set(64))
print(single_set(63))
print()

'''
TC - O(1)
if N&(N-1) == 0, n is a power of 2
'''
def single_set2(n):
    if n == 0:
        return False
    return n&(n-1) == 0

print(single_set2(64))
print(single_set2(65))