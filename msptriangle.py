# Question: find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# algorithm logic:
# 1. Get the length of the array.
# 2. Check if the length of the array is 1.
# 3. If true, return the first element in the array.
# 4. Create a 2D array to store the minimum path sum.
# 5. Loop through the array.
# 6. Loop through the array.
# 7. Get the minimum path sum.
# 8. Return the minimum path sum.
# time complexity: O(n^2)
class Solution():
	def minimumTotal(self, a):
		depth = len(a)
		if depth == 1:
			return a[0][0]

		DP = [[0]*(depth+1) for _ in range(depth+1)]
		
		for level in range(depth-1, -1, -1):
			for i in range(level+1):
				DP[level][i] = a[level][i] + \
				min(DP[level+1][i], DP[level+1][i+1])

		return DP[0][0]

q = Solution()
print(q.minimumTotal([[-1],[2,3],[1,-1,-3]]))
