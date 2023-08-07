def sortedArray(A: [int], B: [int]) -> [int]:

    """
        TC - O(N)
        SC - O(N)
    """
    # Write your code here
    
    idx = 0
    s = set()
    d = dict()

    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            if A[i] not in s:
                s.add(A[i])
                d[idx] = A[i]
                idx += 1
            i += 1
        
        else:
            if B[j] not in s:
                s.add(B[j])
                d[idx] = B[j]
                idx += 1
            j += 1

    while i < len(A):
        if A[i] not in s:
            s.add(A[i])
            d[idx] = A[i]
            idx += 1
        i += 1

    while j < len(B):
        if B[j] not in s:
            s.add(B[j])
            d[idx] = B[j]
            idx += 1
        j += 1

    ans = [0] * len(s)
    ans_idx = 0

    for i in range(idx + 1):
        if d.get(i):
            ans[ans_idx] = d.get(i)
            ans_idx += 1

    return ans



if __name__ == "__main__":
    # A = [1, 2, 3, 4, 6]
    # B = [2, 3, 5]

    A = [1,2,3,3]
    B = [2,2,4]

    print(sortedArray(A, B))