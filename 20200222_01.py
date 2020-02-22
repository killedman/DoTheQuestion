#! /usr/bin/env python

"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:

输入: "A"
输出: 1

示例 2:

输入: "AB"
输出: 28

示例 3:

输入: "ZY"
输出: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        letter_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
                       'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                       'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                       'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                       'Y': 25, 'Z': 26}
        number = 0
        if s is None:
            return 0
        s_list = list(s)
        s_list.reverse()
        len_s_list = len(s_list)
        for i in range(len_s_list):
            number += 26 ** i * letter_dict[s_list[i]]
        return number


if __name__ == "__main__":
    ss = 'ZZZ'
    solution = Solution()
    result = solution.titleToNumber(ss)
    print(result)
