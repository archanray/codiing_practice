class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        given n, k,
        return all possible combinations of k numbers
        chosen from the range [1,n]
        easy O(n^2) solution
        """
        output, temp = [], []
        def backtrack(n, k, num):
            if len(temp) == k:
                output.append(temp.copy())
            for i in range(num, n+1):
                temp.append(i)
                backtrack(n,k,i+1)
                temp.pop()
        backtrack(n,k,1)
        return output

q = Solution()
print(q.combine(4,2))
