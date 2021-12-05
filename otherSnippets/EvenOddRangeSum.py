'''
arr = [1,2,3,4,5,6,7]
if query - [1,4,'e'] - sum of all even-indexed elements b/t range [1,4] otherwise odd-indexed

TC - O(N) | SC - O(N)
'''

def odd(arr):
    ans = [0]*len(arr)
    for i in range(1,len(arr)):
        if i&1:
            ans[i] = ans[i-1] + arr[i]
        else:
            ans[i] = ans[i-1]
    return ans

def even(arr):
    ans = [0]*len(arr)
    ans[0] = arr[0]
    for i in range(1,len(arr)):
        if i&1:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + arr[i]
    return ans

arr = [1,2,3,4,5,6,7]
query = [[0,5,'e'],[0,5,'o']]

odd = odd(arr)
even = even(arr)

for i in query:
    if i[-1] == 'e':
        print(even[i[1]] - even[i[0]])
    else:
        print(odd[i[1]] - odd[i[0]])