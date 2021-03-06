#! /usr/bin/env python

"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 1:
            return 0
        multi_nu_list = list(range(1, n+1))
        while len(multi_nu_list) >= 2:
            multi_nu_list[0] = multi_nu_list[0] * multi_nu_list[1]
            multi_nu_list.pop(1)
        multi_result = str(multi_nu_list[0])
        tmp_index = []
        for i in range(1, 9):
            if multi_result.rfind(str(i)) > -1:
                tmp_index.append(multi_result.rfind(str(i)))
        return len(multi_result) - 1 - max(tmp_index)

if __name__ == "__main__":
    # 解决7304的超时问题后，数字是7563时，会超过leetcode的时间限制；
    num = 7563
    solution = Solution()
    result = solution.trailingZeroes(num)
    print(result)
