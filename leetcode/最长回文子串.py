# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
# 动态规划 时间超限
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ""
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                l = j+i
                if l>=n:continue
                # print(j,l)
                if j==l:
                    dp[j][l] = True
                elif j+1 ==l:
                    dp[j][l] = s[j]==s[l]
                else:
                    dp[j][l] = (s[j]==s[l]) and dp[j+1][l-1]

                if dp[j][l] and l-j+1>len(ans):
                    ans = s[j:l+1]
        return ans



s = "babad"
S =Solution()
res= S.longestPalindrome(s)
print(res)