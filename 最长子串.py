#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 16:27:33
# @Author  : wanpeng 
"最长子串"

def longestsubstring(s):
	j=0
	maxlen=0
	used={}
	for i in range(len(s)):
		if s[i] in used:
			j = max(j,used[s[i]]+1)
		maxlen = max(maxlen,i-j+1)
		used[s[i]]=i
	return maxlen

if __name__=="__main__":
	print longestsubstring("pwwdee")
