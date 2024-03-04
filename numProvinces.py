# LC: medium
class Solution():
	def dfs(self, start):
		if self.visited[start] == 0:
			self.visited[start] = 1
			for j in range(self.n):
				if self.isConnected[start][j] == 1:
					self.dfs(j)
	def findCircleNum(self, isConnected):
		# finding connected components in a graph
		self.isConnected = isConnected
		self.n = len(isConnected)
		self.visited = [0 for _ in range(self.n)]
		if self.n == 0:
			return 0
		count = 0
		for i in range(self.n):
			if self.visited[i] == 0:
				# print(i, self.visited)
				self.dfs(i)
				count += 1
		return count

inputs = [[1,0,0],[0,1,0],[0,0,1]]
q = Solution()
print(q.findCircleNum(inputs))