#! /usr/bin/env python
"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    """质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的
    数叫做质数；否则称为合数；"""
    def countPrimes(self, n: int) -> int:
        pass_list = []
        if n < 1:
            return 0
        for i in range(2, n):
            if self.check_num(i):
                pass_list.append(i)
        return len(pass_list)

    def check_num(self, nu):
        for j in range(2, nu):
            if nu % j == 0:
                return False
        return True


if __name__ == "__main__":
    # 当数目很大时，会非常非常慢，比如499979，leetcode测试会超时
    num = 9999
    solution = Solution()
    result = solution.countPrimes(num)
    print(result)
