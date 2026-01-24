# 1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ans += 1
        return ans

# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits

# remember that i is already each element in the list so no need to do nums[i] and also len() retunr int nor str so no need to convert it again