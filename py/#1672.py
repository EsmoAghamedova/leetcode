# accounts = [[1,5],[7,3],[3,5]]

# num_list = []
# for i in accounts:
#     num = sum(i)
#     num_list.append(num)
# ans = max(num_list)
# print(num_list)
# print(ans)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        num_list = []
        for i in accounts:
            num = sum(i)
            num_list.append(num)
        ans = max(num_list)
        return ans
    
# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/richest-customer-wealth/