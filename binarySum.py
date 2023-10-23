class Solution():
	def binSum(self, str1, str2):
		m, n = len(str1), len(str2)
		# we want str2 to be smaller than str1
		if m < n:
			return self.binSum(str2, str1)
		output = ""
		carry = 0
		j = m-1
		for i in range(n-1, -1, -1):
			if str2[i] == str1[j]:
				if carry == 1:
					output = "1"+output
				else:
					output = "0"+output
				if str2[i] == 1:
					carry = 1
			else:
				if carry == 1:
					output = "0"+output
					carry = 1
				else:
					output = "1"+output
			j = j-1
		# say we have finished adding pairs
		while 
