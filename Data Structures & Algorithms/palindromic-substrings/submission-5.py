class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def stretch(l,r):
            found = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                found += 1
                l -= 1
                r += 1
            return found

        for i in range(len(s)):
           count += stretch(i, i) + stretch(i, i + 1)
        return count

        