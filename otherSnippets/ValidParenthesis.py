class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        for char in A:
            if char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return 0
                var = stack.pop()
                if var == '(':
                    if char != ')':
                        return 0
        if stack: return 0
        return 1