class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(idx, path, cur):
            if cur > target:
                return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0,[],0)
        return res

q = Solution()
print(q.combinationSum2([10,1,2,7,6,1,5], 8))
print(q.combinationSum2([2,5,2,1,2], 5))