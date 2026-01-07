# nums = [1,2,3,1,1,3]

# m = []
# pair = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j]:
#             pair += 1
# ans = pair
# print(ans)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = []
        pair = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    pair += 1
        ans = pair
        return ans
    
