arr = [1, 1, 1]
cnt = 0

EvenSum  = 0
OddSum = 0
for i in range(len(arr)):
    if i&1:
        OddSum += arr[i]
    else:
        EvenSum += arr[i]

'''
- Now iterate over elements and compare sum while removing current element
- If odd-indexed element is removed, all the even-indexed in the right become odd-indexed
'''
CurrEvenSum = arr[0]  #zero index element is even, of course
CurrOddSum = 0

IterateEvenSum = 0
IterateOddSum  = 0

#Checking for index 0 after removing it
if OddSum == EvenSum - arr[0]:
    cnt += 1

#Checking for index 1 to N
for i in range(1,len(arr)):
    if i&1: # i is odd 
        CurrOddSum += arr[i]
        IterateOddSum = CurrOddSum + ( EvenSum - CurrEvenSum ) - arr[i]
        IterateEvenSum= CurrEvenSum + ( OddSum - CurrOddSum )
    else: # i is even
        CurrEvenSum += arr[i]
        IterateEvenSum = CurrEvenSum + ( OddSum - CurrOddSum ) - arr[i]
        IterateOddSum  = CurrOddSum + ( EvenSum - CurrEvenSum )
    
    if IterateEvenSum == IterateOddSum:
        cnt += 1
print(cnt)