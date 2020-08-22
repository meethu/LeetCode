class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        s = re.findall("\w", s)
        return s == s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

# class Solution:
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = ''.join(filter(str.isalnum,s)).lower()
#         return s == s[::-1]
