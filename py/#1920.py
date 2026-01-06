# 1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
    
# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/build-array-from-permutation?q=1920