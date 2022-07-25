"""
Title: Reverse String
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
Grade: Easy
Tags: string
"""
from typing import List

input1 = ["h", "e", "l", "l", "o"]
output1 = ["o", "l", "l", "e", "h"]
# input2 =
# output2 =
# input3 =
# output3 =
# input4 =
# output4 =

class Solution:
    def some_problem(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            left_char = s[i]
            s[len(s) - i - 1], s[i] = left_char, s[len(s) - i - 1]
        return s


self = Solution()
result1 = Solution.some_problem(self, input1)
assert result1 == output1, print('Result', result1, 'Expected', output1)
# result2 = Solution.some_problem(self, input2)
# assert result2 == output1, print('Result', result2, 'Expected', output2)
# result3 = Solution.some_problem(self, input3)
# assert result3 == output1, print('Result', result3, 'Expected', output3)
# result4 = Solution.some_problem(self, input4)
# assert result4 == output1, print('Result', result4, 'Expected', output4)

print('All done!')
