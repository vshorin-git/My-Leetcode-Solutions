# Title: Plus One
# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559
# Grade: Easy
# Tags: array, recursion

from typing import List


class Solution:
    def some_problem(self, digits: List[int]) -> List[int]:
        if len(digits) > 1:
            if digits[-1] == 9:
                digits[-1] = 0
                digits[:-1] = self.some_problem(self, digits[:-1])
                return digits
            else:
                digits[-1] = digits[-1] + 1
                return digits
        else:
            if digits[0] == 9:
                return [1, 0]
            else:
                digits[0] = digits[0] + 1
                return digits


self = Solution()
assert Solution.some_problem(self, [1, 2, 3]) == [1, 2, 4]
assert Solution.some_problem(self, [4, 3, 2, 1]) == [4, 3, 2, 2]
assert Solution.some_problem(self, [9]) == [1, 0]

print('All done!')
