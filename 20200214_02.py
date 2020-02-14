#! /usr/bin/env python

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i
        # 以下方法针对测试时超出时间限制进行了优化
        new_nums = sorted(nums)
        while new_nums:
            first = new_nums[0]
            if new_nums.count(first) == 2:
                new_nums = new_nums[2:]
            elif new_nums.count(first) == 1:
                return first


if __name__ == "__main__":
    num_list = [4,1,2,1,2]
    solution = Solution()
    result = solution.singleNumber(num_list)
    print(result)
