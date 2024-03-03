# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.
# algorithm logic:
# 1. Create a stack and push infinity to it.
# 2. Loop through the array.
# 3. Check if the last element in the stack is less than or equal to the current element in the array.
# 4. If true, pop the last element in the stack and multiply it by the minimum of the last element in the stack and the current element in the array.
# 5. Append the current element in the array to the stack.
# 6. Loop through the stack.
# 7. Pop the last element in the stack and multiply it by the last element in the stack.
# 8. Return the result.
class Solution:
    def mctFromLeafValues(self, arr):
        stack = [float('inf')]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

# Time complexity: O(n), where n is the length of arr.
# Space complexity: O(n).
# Test case:
# [6,2,4]
# [4,11]
# [6,2,4,3]
# [6,2,4,3,5]
# [6,2,4,3,5,7]
input = [6,2,4]
print(Solution().mctFromLeafValues(input))