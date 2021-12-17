def mod(a,n,p):
    res = 1
    for i in range(n):
        res *= a%p
    return res%p

print(mod(2,5,9))