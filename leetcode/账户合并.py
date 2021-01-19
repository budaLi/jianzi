# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

import collections

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # 并查集
        # 如果parents[i] == i, 表示当前节点为根节点
        parents = [i for i in range(len(accounts))]

        dic = {}

        def find(x):
            # 找个这个索引的父节点
            root = x
            while root != parents[root]:
                root = parents[root]
            return root

        def union(x, y):
            parents[find(x)] = find(y)

        # 如果邮箱出现过则合并对应的索引
        for index in range(len(accounts)):
            for email in accounts[index][1:]:
                if email not in dic:
                    dic[email] = index
                else:
                    union(dic[email], index)

        users = collections.defaultdict(set)
        res = []
        # 1. users：表示每个并查集根节点的行有哪些邮箱
        # 2. 使用set：避免重复元素
        # 3. 使用defaultdict(set)：不用对每个没有出现过的根节点在字典里面做初始化
        for i in range(len(accounts)):
            for account in accounts[i][1:]:
                users[find(i)].add(account)

        # 输出结果的时候注意结果需按照字母顺序排序（虽然题目好像没有说）
        for key, val in users.items():
            res.append([accounts[key][0]] + sorted(val))

        return res


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
s = Solution()
res= s.accountsMerge(accounts)
print(res)