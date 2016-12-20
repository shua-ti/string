#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 11:27:20
# @Author  : wanpeng
# @Version : 1.0
"去除重复元素"

def removeduplicates(nums,k):
	i=0
	for num in nums:
		if i<k or num > nums[i-k]:
			nums[i]=num
			i+=1
	return nums[:i]
			

if __name__=="__main__":
	print removeduplicates([1,1,2,2,2,3,4,4,5,5],1)
