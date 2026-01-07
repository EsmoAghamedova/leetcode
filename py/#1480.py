# 1480. Running Sum of 1d Array
# Solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        current_sum = 0
        for i in nums:
            current_sum += i
            ans.append(current_sum)
        return ans
        



# Solution 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list(accumulate(nums))
        return ans
        


# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/running-sum-of-1d-array?q=Running+Sum+of+1D+Array