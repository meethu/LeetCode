class Solution:
    def simplifyPath(self, path):
        stack = []
        paths = path.split("/")
        for i in paths:
            if i not in ['', '.', '..']:
                stack.append(i)
            if i == '..':
                stack.pop()
        return "/" + "/".join(stack)


# 测试用例
# "/home/"
# "/../"
# "/a/./b/../../c/"
# "/a/../../b/../c//.//"
# "/a//b////c/d//././/.."

path = "/a//b////c/d//././/.."
problems = Solution()
print(problems.simplifyPath(path))