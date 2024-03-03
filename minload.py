# minimum possible value of max load time of servers if resources are allocated optimally
# example:
# bursttime = [4,3,2,2,2,6], k = 3
# output: 7
# bursttime = [2,3,1,2,4,3], k = 2
# output: 9
# bursttime = [1,2,3,4,5], k = 2
# output: 8
class Solution:
    def minimumTimeRequired(self, jobs, k):
        if k == len(jobs):
            return max(jobs)
    
        self.min_val = float("inf")

        def backtrack(idx,ans):
            if idx == len(jobs):
                self.min_val = min(self.min_val,max(ans))
                return

            seen = set()

            for i in range(k):
                if ans[i] in seen: continue
                if ans[i] + jobs[idx] >= self.min_val: continue
                seen.add(ans[i])

                ans[i] += jobs[idx]
                backtrack(idx+1,ans)
                ans[i] -= jobs[idx]

        backtrack(0,[0]*k)

        return self.min_val

q = Solution()
print(q.minimumTimeRequired([1,2,4,7,8], 2)) # 7
