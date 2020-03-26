# 其实无论是移动短指针和长指针都是一种可行求解。
# 只是，一开始就已经把指针定义在两端，如果短指针不动，而把长指针向着另一端移动，两者的距离已经变小了，
# 无论会不会遇到更高的指针，结果都只是以短的指针来进行计算。 故移动长指针是无意义的。
# 我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。
# 此外，我们会使用变量 maxs 来持续存储到目前为止所获得的最大面积。
# 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxs，并将指向较短线段的指针s向较长线段那端移动一步。


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, maxs = 0, len(height) -1, 0
        while i < j:
            if height[i] <= height[j]:
                maxs = max(maxs, height[i] * (j - i))
                i += 1
            else:
                maxs = max(maxs, height[j] * (j - i))
                j -= 1
        return maxs