class Solution(object):
    def isvalid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {')':'(', ']':'[', '}':'{' }
        for i in s:
            if i not in paren_map:  # 如果 i 不在设定的 map 里面，那么是左括号，直接加入堆栈
                stack.append(i)
            elif not stack or paren_map[i] != stack.pop(): # 如果 stack 不为空或者输入的元素和堆栈顶端元素不匹配
                return False
        return not stack # 如果括号全部匹配，最后堆栈为空

s = "]"
problems = Solution()
print(problems.isvalid(s))