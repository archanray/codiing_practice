#Given an m x n integers matrix, return the length of the longest increasing path in matrix.
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cache = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if cache[i][j]:
                return cache[i][j]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(x, y))
            cache[i][j] += 1
            return cache[i][j]
        return max(dfs(i, j) for i in range(m) for j in range(n))
#Time complexity: O(m*n)

input = [[9,9,4],[6,6,8],[2,1,1]]
q = Solution()
print(q.longestIncreasingPath(input)) #Output: 4