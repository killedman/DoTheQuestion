#! /usr/bin/env python

"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # nums1中以0为占位符，给nums2的n个元素分配了位置，有多少个n就有多少个0
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums2:
            last_num = nums2.pop(0)
            nums1[nums1.index(0)] = last_num
            # list.sort()原地对列表进行排序
            # sorted(list)排序后返回一个新的列表
            nums1.sort()


if __name__ == "__main__":
    nums_1 = [1, 2, 3, 0, 0, 0]
    nums_2 = [2, 5, 6]
    # nums_1 = [0]
    # nums_2 = [1]
    mn = len([i for i in nums_1 if i > 0])
    nn = len([i for i in nums_2 if i > 0])
    solution = Solution()
    solution.merge(nums_1, mn, nums_2, nn)

