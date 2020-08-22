# 普通栈的 push() 和 pop() 函数的复杂度为 O(1)；而获取栈最小值 min() 函数需要遍历整个栈，复杂度为 O(N) 。
# 可以用一个栈，这个栈同时保存的是每个数字 x 进栈的时候的值 与 插入该值后的栈内最小值。即每次新元素 x 入栈的时候保存一个元组：（当前值 x，栈内最小值）。


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:

        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]