class Solution:
    def reverse(self, x: int) -> int:
        max, min = 2147483647, -2147483648
        if x > max or x < min:
            return 0
        elif x < 0:
            return 0 - int(str(-x)[::-1]) if 0 - int(str(-x)[::-1]) > min else 0
        else:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < max else 0
