class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        return self.approach2(arr, n, d)
        
        
    def approach1(self, arr, n, d):
        """
            Brute Force
            
            TC - O(N)
            SC - O(N)
        """
        d = d % n
        
        temp = [0] * d
        
        for i in range(d):
            temp[i] = arr[i]
            
        # shifting
        for i in range(n - d):
            arr[i] = arr[i + d]

        for i in range(n - d, n):
            arr[i] = temp[i - (n - d)]
        return arr
        
    def approach2(self, arr, n, d):
        """
            Optimal Solution
            
            TC - O(N)
            SC - O(1)
        """
        arr = self.reverse(arr, start = 0, end = d - 1)
        arr = self.reverse(arr, start = d, end = n - 1)
        return self.reverse(arr, start = 0, end = n - 1)
        
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 2

    print(Solution().leftRotate(arr, len(arr), k))