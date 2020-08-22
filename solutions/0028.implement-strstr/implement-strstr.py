class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1