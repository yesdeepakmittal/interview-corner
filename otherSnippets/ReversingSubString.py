s = 'abdeagf'
start = 2
end = 5
l = list(s)
while start <= end:
  l[start],l[end] = l[end],l[start]
  start += 1
  end -= 1

print(''.join(l))
