#! /usr/bin/env python

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.



注意事项：您可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        new_s = list(set(s))
        single_char = []
        for i in range(len(new_s)):
            if s.count(new_s[i]) == 1:
                single_char.append(new_s[i])
        if len(single_char) > 0:
            return min([s.index(j) for j in single_char])
        else:
            return -1


if __name__ == "__main__":
    str1 = "leetcode"
    solution = Solution()
    result = solution.firstUniqChar(str1)
    print(result)

