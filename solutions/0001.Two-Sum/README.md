###  题目描述

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum

### 思路

遍历数组，每访问一个元素，先判断其配对的元素是否在 Hash 表中，如果在的话就说明我们找到了答案，将其输出即可，如果没有找到，就将当前的元素放入 Hash 表中，以便后续元素配对。

因为题目要求输出元素在数组中的位置，所以用 HashMap 来存储访问过的元素和其对应的 index。

具体做法：首先创建一个字典，target 和 item 相减，如果目标 result 在字典中，直接返回 res[result],即 result 下标，以及此刻item下标，如果result没有在字典中，那么将此时进行的item（值），以及index(键)存入字典 res

**时空复杂度**
由于使用了 Hash 表，空间复杂度是 O(n) 的，另外就是最差的情况，数组中的每个元素都要遍历到，因此时间复杂度也是 O(n)。

![two-sum](two-sum.gif)

(图片来自： https://github.com/MisterBooo/LeetCodeAnimation)

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



```python
# 变形，输出所有可能的答案
class Solution():

    def twosum(self, nums, target):
        tmp = {}   # 创建字典
        res = []
        for index, item in enumerate(nums):
            result = target - item
            if result in tmp:  # 如果 result 恰好在字典内，直接返回，否则将此时的item放入字典
                res.append([tmp[result], index]) # 创建一个列表，存储所有符合条件的元素
            tmp[item] = index
        return res
```

