# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.parent[x_root] = y_root
        self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def removeStones(self, stone):
        uf = UnionFind()
        n = len(stones)
        for x, y in stones:
            uf.union(x, y + 10001)
        print(uf.parent)
        return n - uf.get_count()



stones =[[0,1],[1,0],[1,1]]
s = Solution()
res = s.removeStones(stones)
print(res)
