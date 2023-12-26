class Solution():
    def countSameTriplet(self, nums):
        """
        Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

        Input: 
        N = 4 
        arr[] = {1, 5, 3, 2}
        Output: 2 
        Explanation: There are 2 triplets:
        1 + 2 = 3 and 3 +2 = 5

        Input: 
        N = 3
        arr[] = {2, 3, 4}
        Output: 0
        Explanation: No such triplet exits
        """
        nums = sorted(nums)
        n = len(nums)
        triplets = []
        for i in range(n-1,-1,-1):
            a = nums[i]
            left = 0
            right = i-1
            targetSum = a
            while left < right:
                print(a, nums[left], nums[right])
                currentSum = nums[left] + nums[right]
                if currentSum == targetSum:
                    triplets.append([a, nums[left], nums[right]])                
                elif currentSum < targetSum:
                    left = left+1
                else:
                    right = right-1
        return triplets

arr = [1, 5, 3, 2]
q = Solution()
print(q.countSameTriplet(arr))
