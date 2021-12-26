n = 64
ans = []
while n>0:
  ans.append(n%2)
  n //= 2
print(ans[::-1])
print(bin(64))