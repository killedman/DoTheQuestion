#! /usr/bin/env python

"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3

示例 2:

输入: a = -2, b = 3
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # if a < 0:
        #     print(format(2*64 + a, 'b'))
        #     # a = self.add(~a, 1)
        # if b < 0:
        #     b = self.add(~b, 1)
        return self.add(a, b)

    def add(self, aa, bb):
        # print(aa, bb)
        # 异或位运算符是无进位的按位相加
        result_plus = aa ^ bb
        # 与位运算符加上左移一位运算符等于进位
        carry = (aa & bb) << 1
        # 如果进位不等于0，将两者按照之前的步骤再进行一次
        while carry != 0:
            c = result_plus
            d = carry
            result_plus = c ^ d
            carry = (c & d) << 1
        return result_plus



if __name__ == "__main__":
    ss = -2
    tt = 3
    solution = Solution()
    result = solution.getSum(ss, tt)
    print(result)
