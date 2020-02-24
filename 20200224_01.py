#! /usr/bin/env python
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return_list = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return return_list
        count = 2
        while count < numRows:
            # print(return_list)
            count = count + 1
            last_list = return_list[-1]
            temp_list = []
            for i in range(0, len(last_list)-1):
                temp_list.append(last_list[i] + last_list[i+1])
            temp_list.insert(0, last_list[0])
            temp_list.append(last_list[-1])
            return_list.append(temp_list)
        return return_list



if __name__ == "__main__":
    ss = 0
    solution = Solution()
    result = solution.generate(ss)
    print(result)
