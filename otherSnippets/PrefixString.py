s = ['abacadabra','abacus']
from functools import cmp_to_key

def my_cmp(a,b):
  if len(a) < len(b):
    return -1
  if len(a) > len(b):
    return 1
  return 0

s.sort(key=cmp_to_key(my_cmp))
print(s)
ans = ''

# for i in range(len(s[0])):
#   for j in s[1:]:
#     if s[0][i] == j[i]:
#       pass
#     else:
#       print(ans[:-1])
#       break
#     ans += s[0][i]
# print(ans)
for i in range(len(s[0])):
  if s[0][i] == s[1][i]:
    ans += s[0][i]
  else:
    break
print(ans)