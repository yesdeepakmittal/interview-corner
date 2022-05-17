#https://practice.geeksforgeeks.org/problems/product-of-array-element/1/
def product(arr,n,mod):
    # your code here
    ans = 1
    for i in range(n):
        ans *= (arr[i]%mod)
    return ans%mod