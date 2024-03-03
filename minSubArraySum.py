# LC: medium
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

