class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        self.dfs(candidates, target, [], result)
        return result
    def dfs(self, nums, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], result)

q = Solution()
print(q.combinationSum([2], 1))