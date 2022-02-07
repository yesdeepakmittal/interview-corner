def is_palindrome(a):
    start = 0
    end = len(a)-1
    while start <= end:
        if a[start] == a[end]:
            # pass
            start += 1
            end -= 1
        else:
            return False
    return True
l = ['nitin','liril','abac','Python']
for i in l:
    if is_palindrome(i):
        print(i,'is Palindrome String')
    else:
        print(i,'is not a Palindrome String')
print()
print()

#Longest Palindrome Sub-String
''''
Brute Force
TC - O(N3)
total no. of substrings are n*(n+1)/2
'''
s = 'abacab'
mx = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if is_palindrome(s[i:j+1]):
            if len(s[i:j+1]) > mx:
                mx = len(s[i:j+1])
                ans = s[i:j+1]
print('Maximum length of Palindromic SubString in',s,'is',mx,ans)