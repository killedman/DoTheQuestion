#! /usr/bin/env python

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        tmp_set = set()
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        # print('min_len is {0}'.format(min_len))
        for i in range(min_len):
            for s in strs:
                tmp_set.add(s[i])
            if len(tmp_set) == 1:
                # print(tmp_set)
                common_prefix += list(tmp_set)
                tmp_set = set()
            else:
                break
        # print(''.join(common_prefix))
        if len(common_prefix) == 0:
            return ""
        return ''.join(common_prefix)





if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonPrefix(['float', 'flow'])
