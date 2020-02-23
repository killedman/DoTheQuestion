#! /usr/bin/env python

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for r in list(s):
            # 过滤非数字和字母的元素
            if r.isalpha() or r.isdigit():
                if r.isalpha():
                    # 将字母全部转成小写字母
                    s_list.append(r.lower())
                else:
                    s_list.append(r)
        raw_s = ''.join(s_list)
        s_list.reverse()
        new_s = ''.join(s_list)
        # print(raw_s, new_s)
        if raw_s == new_s:
            return True
        else:
            return False


if __name__ == "__main__":
    ss = "0P"
    solution = Solution()
    result = solution.isPalindrome(ss)
    print(result)
