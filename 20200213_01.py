#! /usr/bin/env python

"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fizz-buzz
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out_list.append("FizzBuzz")
            elif i % 3 == 0:
                out_list.append("Fizz")
            elif i % 5 == 0:
                out_list.append("Buzz")
            else:
                out_list.append(str(i))
        return out_list


if __name__ == "__main__":
    num = 5
    solution = Solution()
    result = solution.fizzBuzz(num)
    print(result)