"""
Title:  Valid Palindrome
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
Grade: Easy
Tags: strings
"""
s = "A man, a plan, a canal: Panama"
output1 = True
s2 = "race a car"
output2 = False
s3 = " "
output3 = True


class Solution:
    def some_problem(self, s: str) -> bool:
        string = ''.join(char for char in s.lower() if char.isalnum())
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True


self = Solution()
result1 = Solution.some_problem(self, s)
assert result1 == output1, print('Result', result1, 'Expected', output1)
result2 = Solution.some_problem(self, s2)
assert result2 == output2, print('Result', result2, 'Expected', output2)
result3 = Solution.some_problem(self, s3)
assert result3 == output3, print('Result', result3, 'Expected', output3)

print('All done!')
