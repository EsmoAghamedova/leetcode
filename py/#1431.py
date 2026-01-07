# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        m = max(candies)
        for x in candies:
            boolean = (x + extraCandies) >= m
            ans.append(boolean)

        return ans

# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies