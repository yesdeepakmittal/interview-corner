def method1(s):
  '''
  TC - O(NlogN) sorting
  '''
  arr = list(s)

  for i in range(len(arr)):
    arr[i] = ord(arr[i])

  arr.sort()
  for i in range(len(arr)):
    arr[i] = chr(arr[i])
  print(''.join(arr))

def method2(s):
  '''
  TC - O(N) -> 26*N -> N
  '''
  ans = ''
  for i in range(97,123):
    for j in s:
      if chr(i) == j:
        ans += j
  print(ans)

def method3(s):
  '''
  TC - O(N) -> N + N
  '''
  ans = ''
  d = {}
  for i in s:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  for i in range(26):
    if chr(i+97) not in d:
      continue
    else:
      for j in range(d[chr(i+97)]):
        ans += chr(i+97)
  print(ans)

def method4(s):
  '''
  TC - O(N) -> N + N
  '''
  ans = ''
  l = [0]*26
  for i in s:
    l[ord(i) - 97] += 1
  for i in range(26):
    for j in range(l[i]):
      ans += chr(i + 97)
  print(ans)
  

s = 'dabcaedb'
method1(s)
method2(s)
method3(s)
method4(s)