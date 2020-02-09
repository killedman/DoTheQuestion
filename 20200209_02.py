#! /usr/bin/env python

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 这个题看别人的解释，实际是一个斐波那契数列
    # f(n) = f(n-1) + f(n-2)
    # 直接使用斐波那契数列的数列，比如：1,1,2,3,5,8...
    # 效率比原先直接使用递归提高了很多
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        left = 1
        right = 2
        for i in range(3, n+1):
            left, right = right, left + right
        return right




if __name__ == "__main__":
    solution = Solution()
    result = solution.climbStairs(35)
    print(result)
