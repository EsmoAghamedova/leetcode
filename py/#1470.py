# 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0, n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans
    
# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/shuffle-the-array?q=Shuffle+the+Array