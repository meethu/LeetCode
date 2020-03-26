# 交换律：a ^ b ^ c <=> a ^ c ^ b
# 任何数于0异或为任何数 0 ^ n => n
# 相同的数异或为0: n ^ n => 0


# 代码参考热评。解释下：假设有一个数为x,那么则有如下规律：
# 0 ^ x = x,

# x ^ x = 0；

# x & ~x = 0,

# x & ~0 =x;

# -那么就是很好解释上面的代码了。一开始a = 0, b = 0;

# x第一次出现后，a = (a ^ x) & ~b的结果为 a = x, b = (b ^ x) & ~a的结果为此时因为a = x了，所以b = 0。

# x第二次出现：a = (a ^ x) & ~b, a = (x ^ x) & ~0, a = 0; b = (b ^ x) & ~a 化简， b = (0 ^ x) & ~0 ,b = x;

# x第三次出现：a = (a ^ x) & ~b， a = (0 ^ x) & ~x ,a = 0; b = (b ^ x) & ~a 化简， b = (x ^ x) & ~0 , b = 0;

# 所以出现三次同一个数，a和b最终都变回了0.

# 只出现一次的数，按照上面x第一次出现的规律可知a = x, b = 0;因此最后返回a.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b

# 参考热评的答案。使用位运算，就是只看某一位，比如只看最后一位，其出现情况与其他位无关。
# 出现三次将它消掉，那么一个数出现一次和出现两次肯定是不一样的状态，因为如果状态一样，那么再次出现这个数，
# 不知道一共出现了两次还是三次。所以，在整个状态的变换中有三种状态，也就是出现一次，出现两次，出现三次（出现零次），
# 所以要用三个状态才能表示。因此采用两个数字进行状态的标注。 热评中采用了00标记出现一次和出现零次，用01标注出现一次，
# 用10标注出现两次，这是最直观的表达，其实也可以用10标注出现一次，01标注出现两次，甚至是可以用11标注出现两次
# （因为数组中没有出现两次的，所以最后其实也只要看第二个数就可以了）。
# 它只是表示一个状态，和具体的数字没有关系，但是出现零次和出现三次必须要用00来表示。
# 标注好了状态之后，它其实就是一个状态的转移函数，现在考虑输入，输入有三个，分别是a，b还有新的数x。
# 也就是ab的状态变化除了要看新来的数x，还要看原来ab的状态。按照最直观的状态分类（一次==01，两次==10，三次==0），
# 现在写出它的真值表，注意当x为0时，ab的值不变，先更新b，再更新a，其实也可以先更新a，再更新b，
# 只要更新b的之后用更新之后的a就可以了。

# a b x | b
# 0 0 1 1
# 0 1 1 0
# 1 0 1 0
# 0 0 0 0
# 0 1 0 1
# 1 0 0 0
# 这是b的真值表，用了数电中的表达方式，所以b = a'.b'.x+a'.b.x'=a'.(b⊕x)。 现在考虑a的真值表，此时状态中的b是更新之后的值

# a b x | a
# 0 1 1 0
# 0 0 1 1
# 1 0 1 0
# 0 0 0 0
# 0 1 0 0
# 1 0 0 1
# 这是b的真值表，所以a=a'.b'.x+a.b'.x'=b'.(a⊕x)。 因为b是表示出现一次的值，所以最终的b就是需要的结果，这也就是最终的结果。
# 上述就是热评代码的一个推导过程，换成其他的状态，甚至是有更多的状态都可以用这种方法来推导。代码大同小异.