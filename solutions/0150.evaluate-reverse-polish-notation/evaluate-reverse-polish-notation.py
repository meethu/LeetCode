# python的 b / a 会向下取整， 比如 -1 / 132 = -1。 题目要求是取整数部分，那么负数的时候，实际应该是向上取整， 解决方法： int(b / float(a))

# python3 b / a 会转为小数计算，所以直接 int(b / a)， 不能 b // a


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f1 = lambda a, b: a + b
        f2 = lambda a, b: a - b
        f3 = lambda a, b: a * b
        f4 = lambda a, b: int(a / b)
        maps = {'+': f1, '-': f2, '*': f3, '/': f4}
        stack = []
        for i in tokens:
            if i in maps:
                a = stack.pop()
                b = stack.pop()
                stack.append(maps[i](b, a))
            else:
                i = int(i)
                stack.append(i)
        return stack[-1]

#  def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         stack = []

#         for t in tokens:
#             if t in '+-*/':
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 if t == '+':
#                     new_num = num1 + num2
#                 elif t == '-':
#                     new_num = num1 - num2
#                 elif t == '*':
#                     new_num = num1 * num2
#                 elif t == '/':
#                     new_num = int(num1 / num2)
#                 stack.append(new_num)

#             else:
#                 stack.append(eval(t))

#         return stack[0]
