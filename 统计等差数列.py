#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 16:44:38
# @Author  : wanpeng
# @Version : 1.0
"统计序列中等差数列的个数"

def numberOfArithmeticSlices(nums):
	size = len(nums)
	if size<2:
		return 0
	cnt=toatl=0
	for i in range(2,len(nums)):
		if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
			cnt+=1
			toatl+=cnt
		else:
			cnt=0
	return toatl


if __name__=="__main__":
	print numberOfArithmeticSlices([1,2,3,4,6,8,9,10])
