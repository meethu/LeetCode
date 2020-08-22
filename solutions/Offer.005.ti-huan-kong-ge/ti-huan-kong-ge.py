class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = []
        for char in s:
            if char == " ":
                ret.append("%20")
            else:
                ret.append(char)
        return "".join(ret)