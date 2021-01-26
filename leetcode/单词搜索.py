# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 边界
        m = len(board)
        if m==0: return False
        n = len(board[0])
        if n==0:return False

        # 标志当前网格是否已经被使用
        masked = [[False for _ in range(n)] for _ in range(m)]

        # 遍历每一行每一列 如果搜索到则返归true
        for i in range(m):
            for j in range(n):
                if self.search(board,masked,word,0,i,j,m,n):
                    return True
        return False


    def search(self,board,masked,word,index,x,y,m,n):
        """
        :param board: 搜索的网格
        :param masked: 标志当前位置是否被标志
        :param word:  搜索的单词
        :param index:  单词的索引
        :param x:      搜索的起始x
        :param y:      搜索的起始Y
        :return:
        """
        # 上左下右四个方向
        direction = [[0,1],[-1,0],[0,-1],[1,0]]
        # 如果当前索引为单词的最后一个字符 则只要判断当前网格字符和该字符是否相等
        if index==len(word)-1:
            return board[x][y]==word[index]
        # 如果当前字符匹配则继续比较
        if board[x][y]==word[index]:
            # 标志当前位置用过
            masked[x][y] = True

            for _x,_y in direction:
                new_x = x+_x
                new_y = y+_y
                # 判断是否越界  是否被用过  下个单词是否可找到
                if 0<=new_x<m and 0<=new_y<n and not masked[new_x][new_y]  \
                    and self.search(board,masked,word,index+1,new_x,new_y,m,n):
                    return True
            # 如果四个方向都没有 释放masked
            masked[x][y] = False
        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# word = "ABCCED"
# word = "SEE"
word = "ABCB"
s = Solution()
res = s.exist(board,word)
print(res)




