# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = []
        for emp in schedule:
            for start, end in emp:
                intervals.append((start, end))
        intervals.sort()
        res = []
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start > prev:
                res.append([prev, start])
            prev = max(prev, end)
        return res
# Time complexity: O(nlogn)
# Space complexity: O(n)
schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
q = Solution()
print(q.employeeFreeTime(schedule)) # [[5,6],[7,9]]