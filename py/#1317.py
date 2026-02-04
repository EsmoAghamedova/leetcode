# 1317. Convert Integer to the Sum of Two No-Zero Integers


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for a in range(1, n):
            b = n - a
            if "0" not in str(a) and "0" not in str(b):     #remeber not, in, and, or and etc. is in py
                return [a, b]

# I haven't list here but in leetcode you can try it directly.
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-in
