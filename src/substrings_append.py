"""
Substrings
Given a string s, check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together.
"""
from typing import List


class SolutionNaive:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring_candidate = ""
        for i, c in enumerate(s):
            if i >= len(s) // 2:
                break
            substring_candidate += c
            substring_result = substring_candidate
            n = len(substring_result)
            while n < len(s):
                substring_result += substring_candidate
                n = len(substring_result)

            print(substring_result)
            if substring_result == s:
                return True
        return False


class Solution:
    def prefixFunction(self, s: str) -> List[int]:
        """Preprocessing step

        Longest proper prefix that is also a suffix, this is part
        of KMP algorithm (Knuth-Morris-Pratt)

        :param s: Input strng
        :type s: str
        :return: Prefix function as pre-processing step
        :rtype: List[int]
        """
        m = len(s)
        pi = [0] * m
        pi[0] = 0
        k = 0
        for q in range(1, m):
            while k > 0 and s[k] != s[q]:
                k = pi[k - 1]

            if s[k] == s[q]:
                k += 1
            pi[q] = k

        return pi

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        pi = self.prefixFunction(s)

        # Length of proper prefix that is also a suffix
        m = pi[len(s) - 1]
        return m > 0 and len(s) % (len(s) - m) == 0


print(Solution().prefixFunction("AABAACAABAA"))
print(Solution().prefixFunction("ABABACA"))
