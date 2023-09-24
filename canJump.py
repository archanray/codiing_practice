class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        max_reach = 0
        nmo = len(nums)-1
        # BFS
        for i in range(nmo):
            current_reach = nums[i]+i
            if max_reach == current_reach and i >= current_reach:
                return False
            max_reach = max(max_reach, current_reach)
            if max_reach >= nmo:
                return True
            # print(i, max_reach, current_reach)
        return False
            
q = Solution()
print(q.canJump([2,1,2,2,1,2,2,2]))