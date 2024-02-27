# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words):
        graph = defaultdict(list)
        indegree = Counter({c: 0 for word in words for c in word})
        for i in range(len(words) - 1):
            for a, b in zip(words[i], words[i + 1]):
                if a != b:
                    graph[a].append(b)
                    indegree[b] += 1
                    break
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = ''
        while queue:
            c = queue.popleft()
            res += c
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == len(indegree) else ''
# Time complexity: O(C)
# Space complexity: O(C)
words = ["z","x","z"]
q = Solution()
print(q.alienOrder(words)) # ""