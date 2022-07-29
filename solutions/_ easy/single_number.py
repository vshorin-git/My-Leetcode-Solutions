# Title: Single Number
# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
# Grade: Easy
# Tags: array,
from typing import List


class Solution:
    def some_problem(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result ^= number
        return result



self = Solution()
assert Solution.some_problem(self, [2, 2, 1]) == 1
assert Solution.some_problem(self, [4, 1, 2, 1, 2]) == 4
assert Solution.some_problem(self, [1]) == 1

print('All done!')
