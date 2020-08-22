class Solution:
    def longestCommonPrefix(self, s):
        if not s:
            return ""
        res = s[0]  # 将result设置为字符串第一个单词
        i = 1  # 从第一个字符串开始比较
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1
        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return ""
        ss = map(set, zip(*strs))  # 去重
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


# 利用python的max()和min()，在Python里字符串是可以比较
# 按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
# 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


if __name__ == "__main__":
    s = ["racecar", "dog", "car"]
    print(Solution().longestCommonPrefix(s))
