#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 11:27:20
# @Author  : wanpeng
# @Version : 1.0
"去除重复元素"

def removeduplicates(nums):
	if nums==None:
		return 0
	i=j=0
	size = len(nums)
	while i<size and j < size:
		while j<size and nums[i]==nums[j]:
			j+=1
		i+=1
		if j<size:
			nums[i]=nums[j]
		
	return i
			

if __name__=="__main__":
	print removeduplicates([1,1,2,2,2,3,4,4,5,5])
