#! /usr/bin/env python

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
参考： https://www.technotification.com/2018/08/singly-linked-list-python-programming.html 学习链表知识
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #将列表转换为单链链表
    def initList(self, data):
        if len(data) == 0:
            return
        else:
            self.head = ListNode(data[0])
            #设置一个虚拟头部节点preHead指向原始的位置，指针pre用于跟踪next
            prehead = self.head
            pre = self.head
            for i in data[1:]:
                node = ListNode(i)
                pre.next = node
                pre = pre.next
            return prehead

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 维护一个虚拟的头部节点，可以随时回到这个跟踪的链表
        preNode = ListNode(-1)
        # 这里还需要一个指针pre；这个地方没有想到；
        pre = preNode
        # l1和l2都不为空时一直循环
        while l1 and l2:
            # 如果l1的第一个节点小于等于l2的第一个节点，preNode.next指向小的节点，也就是l1，l1的当前节点变成l1.next
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            # pre = pre.next 为什么放在while循环里，放在外面就拿不到前面的值了，是出了while循环后while内的值就被释放了吗
            #  pre.next指向下一个节点，pre = pre.next意思是pre这个指针移到了下一个节点。
            pre = pre.next
        # if l1 or l2 is none
        pre.next = l1 if l1 is not None else l2
        return preNode.next


if __name__ == "__main__":
    L1 = [1, 2, 4]
    L2 = [1, 3, 4]
    solution = Solution()
    l1 = solution.initList(L1)
    l2 = solution.initList(L2)
    l3 = solution.mergeTwoLists(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next
