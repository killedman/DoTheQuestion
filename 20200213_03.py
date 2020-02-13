#! /usr/bin/env python
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_nums = nums.count(0)
        while zero_nums != 0:
            nums.remove(0)
            nums.append(0)
            zero_nums = zero_nums - 1
        # print(nums)


if __name__ == "__main__":
    num = [0, 0, 1]
    solution = Solution()
    solution.moveZeroes(num)
