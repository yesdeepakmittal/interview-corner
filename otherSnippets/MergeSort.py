def mergeSort(arr):
  def merge(first,second):
    mix = [0]*(len(first) + len(second))
    i = 0
    j = 0
    k = 0
    while i<len(first) and j < len(second):
      if first[i] < second[j]:
        mix[k] = first[i]
        i += 1
      else:
        mix[k] = second[j]
        j += 1
      k += 1
    
    while i<len(first):
      mix[k] = first[i]
      i += 1
      k += 1
    while j<len(second):
      mix[k] = second[j]
      j +=1 
      k += 1
    return mix

  if len(arr) == 1:
    return arr
  mid = len(arr)//2
  left = mergeSort(arr[0:mid])
  right = mergeSort(arr[mid:len(arr)])
  return merge(left,right)

arr = [3,4,1,2,3,4]
print(mergeSort(arr))