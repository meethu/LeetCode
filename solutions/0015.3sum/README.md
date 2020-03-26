###  题目描述

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum

### 思路
　首先对原数组进行排序，然后开始遍历排序后的数组，这里注意不是遍历到最后一个停止，而是到倒数第三个就可以了，中间如果遇到跟前一个数相同的数字就直接跳过。对于遍历到的数，如果大于0则跳到下一个数，因为三个大于0的数相加不可能等于0；否则用0减去这个数得到一个sum，我们只需要再之后找到两个数之和等于sum即可，这样一来问题又转化为了求two sum，这时候我们一次扫描，找到了等于sum的两数后，加上当前遍历到的数字，按顺序存入结果中即可，然后还要注意跳过重复数字。时间复杂度为 O(n2)

### 代码

* 语言支持：Python

```python
# Hash 表
class Solution():

    def twosum(self, nums, target):
        res = {}   # 创建字典
        for index, item in enumerate(nums):
            result = target - item
            if result in res:  # 如果result好办在字典内，直接返回，否则将此时的item放入字典
                return res[result], index
            res[item] = index
        return None

nums = [2, 7, 11, 15]
target = 9

problems = Solution()
print(problems.twosum(nums, target))
```


