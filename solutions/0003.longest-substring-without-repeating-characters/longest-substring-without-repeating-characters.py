# 解法1
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0

        window = []  # 滑动窗口数组
        max_length = 0  # 最长串长度

        # 遍历字符串
        for c in s:
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in window:
                # 使用当前字符扩展窗口
                window.append(c)
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                window[:] = window[window.index(c) + 1:]
                # 扩展窗口
                window.append(c)

            # 更新最大长度
            max_length = max(len(window), max_length)

        return max_length if max_length != 0 else len(s)


# 解法2
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        ignoreIndex, result = -1, 0
        for idx, v in enumerate(s):
            # 如果这个字符在字典中，那么就把之前的下标存到 ignoreIndex 中，将对应字符的 value 变更为新的下标
            if v in dic and dic[v] > ignoreIndex:
                ignoreIndex = dic[v] # 如果val恰好在tmp字典，那么直接返回忽略的下标
                dic[v] = idx # 如果val恰好在tmp字典，那么直接返回忽略的下标
            else:
                dic[v] = idx
            # 更新长度
            result = max(result, idx - ignoreIndex)
        return result


s = "abcabcbb"
problems = Solution()
print(problems.lengthOfLongestSubstring(s))
