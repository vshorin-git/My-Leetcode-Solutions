"""
Title:  Valid Anagram
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
Grade: Easy
Tags: strings
"""

s = "anagram"
t = "nagaram"
output1 = True
s2 = "rat"
t2 = "car"
output2 = False


class Solution:
    def some_problem(self, s: str, t: str) -> bool:
        t = list(t)
        if len(s) != len(t):
            return False
        for char in s:
            if char in t:
                t.remove(char)
        if t:
            return False
        return True


self = Solution()
result1 = Solution.some_problem(self, s, t)
assert result1 == output1, print('Result', result1, 'Expected', output1)
result2 = Solution.some_problem(self, s2, t2)
assert result2 == output2, print('Result', result2, 'Expected', output2)

print('All done!')
