from copy import copy
class Solution():
	def kPalindromeCheck(self, string, k):
		# check if a string can be palindrome after removing k chars
		n = len(string)
		if n == 0:
			return True
		stringRev = string[-1::-1]
		# now solve the longest common subsequence problem!
		m = copy(n)
		DP = [[0]*(m+1)]*(n+1)
		for i in range(1,m+1):
			for j in range(1,n+1):
				if stringRev[i-1] == string[j-1]:
					DP[i][j] = DP[i-1][j-1]+1
				else:
					DP[i][j] = max(DP[i-1][j], DP[i][j-1])
		lenPal = DP[m][n]
		if lenPal + k == n:
			return True
		else:
			return False
		
intputStr = "acdcb"
K = 1
q = Solution()
print(q.kPalindromeCheck(intputStr, K))