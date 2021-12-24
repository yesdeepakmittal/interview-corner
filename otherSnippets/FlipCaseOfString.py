s = 'DeePaK'
arr = list(s)
for i in range(len(s)):
  if ord(arr[i]) >= ord('A') and ord(arr[i]) <= ord('Z'):
    arr[i] = chr(ord(arr[i]) + 32)
  elif ord(arr[i]) >= ord('a') and ord(arr[i]) <= ord('z'):
    arr[i] = chr(ord(arr[i]) - 32)
print(''.join(arr))

s = 'DeePaK'
arr = list(s)
for i in range(len(s)):
  arr[i] = chr(ord(arr[i])^32)
print(''.join(arr))