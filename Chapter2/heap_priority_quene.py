# coding=utf-8
# PRIORITY QUENE ALGORITHM
# 优先级队列是一种用来维护由一组元素构成的集合S的数据结构，这一组元素中的每一个都有一个关键字key。一个最大优先级队列支持以下操作

# INSERT（S，x） 把元素x插入集合S
# MAXIMUM（S） 返回S中具有最大关键字的元素
# EXTRACT-MAX（S） 去掉并返回S中的具有最大关键字的元素
# INCREASE-KEY（S，x，k） 将元素x的关键字的值增加到k，这里k值不能少于x的原关键字的值

# 最大优先级队列应用：分时计算机上作业调度

from heap import max_heapify
from heap import HEAP_SIZE
from heap import parent

# HEAP-MAXIMUM 
def heap_maximum(A):
	return A[0]

# HEAP-EXTRACT-MAX
def heap_extract_max(A):
	if len(A)<1:
		print('errror-heap underflow')
	max=A[0]
	A[0]=A[len(A)-1]
	# POP MAX(last element)
	A.pop()
	# Before call MAX-HEAPIFY,First set HEAP-SIZE's Value
	HEAP_SIZE['A']=len(A)
	max_heapify(A,0)
	# print(A)
	return max

# HEAP-INCREASE-KEY
def heap_increase_key(A,i,key):
	if key<A[i]:
		print('error-new key is samller than current key')
	if i>= len(A):
		print('error-index out of array range')
	A[i]=key
	while i>0 and A[parent(i)]<A[i]:
		temp=A[i]
		A[i]=A[parent(i)]
		A[parent(i)]=temp
		i=parent(i)
	return A

# MAX-HEAP-INSERT
def max_heap_insert(A,key):
	# THE MIN PRIORITY-0 
	A.append(0)
	heap_increase_key(A,len(A)-1,key)
	return A

# TEST CASE
def test():
	A=[16,14,10,8,7,9,3,2,4,1]
	print('HEAP-MAXIMUM',heap_maximum(A))
	print('HEAP-EXTRACT-MAX',heap_extract_max(A))
	print('HEAP-INCREASE-KEY',heap_increase_key(A,8,15))
	print('MAX-HEAP-INSERT',max_heap_insert(A,90))

# RUN
test()


