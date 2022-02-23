def max_sum(a,n):
    #code here
    mx = 0
    sm = 0
    
    # for i in range(n):
    #     sm = 0
    #     for i in range(n):
    #         sm += i * a[i]
    #     if sm > mx:
    #         mx = sm
    #     a = a[1:] + [a[0]]
    sm = sum(a)
    current_sm = 0
    for i in range(n):
        current_sm += i*a[i]
    ans = current_sm
    
    for i in range(1,n):
        current_sm = current_sm - (sm - a[i-1]) + (a[i-1]*(n-1))
        ans = max(ans,current_sm)
        
    return ans

print(max_sum([8,3,1,2],4))