s1 = 'nameless'
s2 = 'salesmen'

def anagram1(s1,s2):
    # TC - O(N) | SC - O(N)
    if len(s1) != len(s2):
        return False
    hash1 = {}
    hash2 = {}

    for i in s1:
        if i in hash1:
            hash1[i] += 1
        else:
            hash1[i] = 1
    for i in s2:
        if i in hash2:
            hash2[i] += 1
        else:
            hash2[i] = 1
    
    for key in hash1:
        if key not in hash2 or hash1[key] != hash2[key]:
            return False
    return True

def anagram2(s1,s2):
    from collections import Counter
    return Counter(s1) == Counter(s2)

def anagram3(s1,s2):
    # TC -> NlogN + N + NlogN -> NlogN  | SC - O(N)
    return sorted(s1) == sorted(s2)
 
print(anagram1(s1,s2))
print(anagram2(s1,s2))
print(anagram3(s1,s2))
