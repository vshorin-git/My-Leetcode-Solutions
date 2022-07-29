"""
Title:  Reverse Integer
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
Grade: Easy
Tags: string
"""
from typing import List

input1 = 123
output1 = 321
input2 = -123
output2 = -321
input3 = 120
output3 = 21


# input4 =
# output4 =

class Solution:
    def some_problem(self, x: int) -> int:
        is_positive = True
        x = list(str(x))
        if x[0] == '-':
            is_positive = False
            x.pop(0)
        for i in range(len(x) // 2):
            left_char = x[i]
            x[len(x) - i - 1], x[i] = left_char, x[len(x) - i - 1]
        for j in range(len(x)):
            if x[j] == 0:
                x.pop(j)
            else:
                break
        x = int(''.join(x))
        if x >= 2**31:
            return 0
        return x if is_positive else -1 * x


self = Solution()
result1 = Solution.some_problem(self, input1)
assert result1 == output1, print('Result', result1, 'Expected', output1)
result2 = Solution.some_problem(self, input2)
assert result2 == output2, print('Result', result2, 'Expected', output2)
result3 = Solution.some_problem(self, input3)
assert result3 == output3, print('Result', result3, 'Expected', output3)

print('All done!')
