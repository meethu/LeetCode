# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ⋯⋯
# 上面这个数列有什么规律？

# 递归调用
class Solution:
    def countAndSay(self, n: int) -> str:
        result = ""
        count = 1
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        prevResult = self.countAndSay(n-1)
        for i in range(len(prevResult)-1):
            if prevResult[i] == prevResult[i+1]: # 如果 prevResult[i] 和后面的数字相同，count计数
                
                count += 1
                continue
                
            else:
                result += str(count) + prevResult[i]
                count = 1
        result += str(count) + prevResult[i+1]
        return result


# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         count_num = 0
#         num = ''
#         strs = ''
#         for char in self.countAndSay(n-1):
#             if char != num:
#                 if count_num > 0:
#                     strs += str(count_num) + num
#                 count_num = 1
#                 num = char
#             else:
#                 count_num += 1
#         strs += str(count_num) + char
#         return strs
                
    
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n==1:
#             return '1'
#         elif n==2:
#             return '11'
#         x=self.countAndSay(n-1)
#         y=''
#         count=1
#         for i in range(len(x)):
             
#             if i<len(x)-1 and x[i+1]==x[i]:
#                 count+=1
#             else:
#                 y+=str(count)
#                 y+=str(x[i])
#                 count=1
#         return y    
    
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         else:            
#             new_str = ''
#             last_str = self.countAndSay(n-1)  # 获取上次的报数
#             cur = last_str[0]   # 当前要统计的字符，初始值为last_str的首字符
#             cur_t = 0           # 当前字符出现的次数
            
#             for i in last_str:
#                 if i == cur:
#                     # 如果相等，则计数+1
#                     cur_t += 1
#                 else:
#                     # 否则先报一次数，然后重新初始化开始统计
#                     new_str +=str(cur_t) + cur
#                     cur = i
#                     cur_t = 1
#             # 循环结束后，还要再报一次，因为如果最后是以if条件退出循环的，最后几个相同的字符并未报出来
#             new_str += str(cur_t) + cur  
#             return new_str
                
                
# // c++
# class Solution {
# public: string countAndSay(int n) {
#         //递归终止的条件
#         if(n == 1) return "1";
#         string prevResult = countAndSay(n-1);
#         int count = 1;//计数
#         string nowResult;//存放结果
#         for(int i = 0 ; i < prevResult.length();i++){
#             //统计有多少个相同数字
#             if(prevResult[i] == prevResult[i+1]){
#                 count++;
#                 continue;
#             }else{
#                 if( prevResult[i] != prevResult[i + 1]) {
#                     nowResult += to_string(count) + prevResult[i];
#                     //重置开始统计其他的数字
#                     count = 1;
#                 }
#             }
#         }
#        return nowResult;
#     }
# };


n = 5
problems = Solution()
print(problems.countAndSay(n))
