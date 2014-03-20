# coding=utf-8
# Divide and Conquer

import math
import timeit
import random

# Divide 
# A[p..r] => A[p..q],A[q+1..r]
def merge_sort(A,p,r):
	if p < r:
		q = math.floor((p+r)/2)
		# 分治成两个有序的子序列
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		# 归并两个有序的子序列
		merge(A,p,q,r)
		return A

# Conquer
def merge(A,p,q,r):
	# type convert
	p=int(p)
	q=int(q)
	r=int(r)
	# left/right sequence array
	left=A[p-1:q]
	right=A[q:r]
	# @-sentinel card
	left=left+['@']
	right=right+['@']
	# index
	k=p-1
	i=0
	j=0
	while left[i] is not '@' and right[j] is not '@':
		if left[i] <= right[j]:
			A[k]=left[i]
			k+=1
			i+=1
		else:
			A[k]=right[j]
			k+=1
			j+=1
	# append the rest list
	if left[i] is '@':
		A[k:r]=right[j:-1]
	else:
		A[k:r]=left[i:-1]

# test case
def test():
	# random test case
	A=[random.randrange(0,10000000) for i in range(10000)]
	# time:python sort method
	start = timeit.default_timer()
	A1=sorted(A)
	time1 = (timeit.default_timer()-start)

	# time:merge_sort method
	start = timeit.default_timer()
	A2=merge_sort(A,1,len(A))
	time2 = (timeit.default_timer()-start)

	if A1 == A2:
		print('Succeed!',A2)
		print('PYTHON:',time1)
		print('MERGE:',time2)
	else:
		print('Faild!',A2)

# main function
def main():
	test()

# run
main()



