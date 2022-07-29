"""
Title: Reverse String
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
Grade: Easy
Tags: string
"""
from typing import List

input1 = ["h", "e", "l", "l", "o"]
output1 = ["o", "l", "l", "e", "h"]


class Solution:
    def some_problem(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            left_char = s[i]
            s[len(s) - i - 1], s[i] = left_char, s[len(s) - i - 1]
        return s


self = Solution()
result1 = Solution.some_problem(self, input1)
assert result1 == output1, print('Result', result1, 'Expected', output1)

print('All done!')
