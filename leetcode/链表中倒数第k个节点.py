# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        left_head = head
        node_count = 1
        while left_head and node_count<k:
            left_head = left_head.next
            node_count+=1

        while left_head.next:
            head = head.next
            left_head = left_head.next

        return head


S = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
k =2
res = S.getKthFromEnd(head,k)
while res:
    print(res.val)
    res = res.next

