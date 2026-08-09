class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if nums[i] == nums[j] and i != j:
    #                 return True

    #     return False
