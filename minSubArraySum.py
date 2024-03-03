# algorithm logic:
# 1. Create a variable to store the sum of the array.
# 2. Create a variable to store the length of the array.
# 3. Create a variable to store the output.
# 4. Loop through the array.
# 5. Create a variable to store the sum of the current subarray.
# 6. Loop through the array.
# 7. Add the current element to the sum of the current subarray.
# 8. Check if the sum of the current subarray is greater than or equal to the target.
# 9. If true, update the output to the minimum of the current output and the length of the current subarray.
# 10. Loop through the array.
# 11. Subtract the first element in the current subarray from the sum of the current subarray.
# 12. Return the output.
# time complexity: O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        return sub array with smallest length equalling sum
        """
        if sum(nums) < target:
            return 0
        s, l, output = 0, 0, len(nums)

        for r, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[l]
                output = min(output, r-l+1)
                l += 1
        return output

