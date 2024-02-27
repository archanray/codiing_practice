# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
class Solution:
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
# Time complexity: O(C), where C is the total content of words.
# Space complexity: O(1).
# Test case:
# ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# ["kuvp","q"], order = "ngxlkthsjuoqcpavbfdermiywz"
# ["hello","hello"], order = "abcdefghijklmnopqrstuvwxyz"
input = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(input, order))