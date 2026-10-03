class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""

        def stretch(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            odd = stretch(i, i)
            even = stretch(i, i + 1)
            for candidate in (odd, even):
                if len(candidate) > len(best):
                    best = candidate

        return best
        